# Data Model Design

## Situation

You're designing the data model for a new feature or service. Getting the schema right now saves painful migrations later. You need to think about relationships, access patterns, indexing, and how the model evolves as requirements change.

## The Prompt

```
You are a senior engineer designing a data model for a new domain. Optimise for the actual query patterns, not theoretical normalisation purity. Document the entities, relationships, indexes, and the access patterns that drove your decisions. Explain what trade-offs you made and why.

Structure:
1. **Domain overview** — what this data represents in business terms
2. **Access patterns** — the top 5-10 queries the application will run (read and write)
3. **Entity definitions** — each entity with fields, types, constraints, and rationale for key decisions
4. **Relationships** — how entities relate, with cardinality
5. **Indexes** — which indexes you'd create and why (tied to access patterns)
6. **Evolution considerations** — how this model handles likely future requirements
7. **Trade-offs** — what you optimised for and what you sacrificed

Domain: [DESCRIBE_THE_DOMAIN]
Database: [DATABASE_TECHNOLOGY]
Access patterns: [KEY_QUERIES]
Expected scale: [DATA_VOLUME]
```

## Example Input

```
Domain: Multi-tenant project management. Organisations have projects, projects have tasks, tasks have assignees, comments, and status history.
Database: PostgreSQL
Key access patterns: List tasks for a project (filtered by status/assignee), get task detail with comments, dashboard showing task counts by status per project, audit log of status changes
Expected scale: 1,000 orgs, 50K projects, 5M tasks, 20M comments
```

## Example Output

> **Data Model: Project Management**
>
> **Access Patterns (driving design decisions)**
> 1. List tasks for project X where status = "in_progress" → frequent, must be fast
> 2. Get task detail with latest 20 comments → frequent, joined query
> 3. Dashboard: count tasks by status for each project in org Y → medium frequency, aggregate
> 4. All tasks assigned to user Z across all projects → medium frequency
> 5. Audit log: status changes for task T → infrequent, append-heavy
> 6. Search tasks by title/description → medium frequency, text search
>
> **Entities**
>
> ```sql
> organisations (
>   id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
>   name        text NOT NULL,
>   slug        text UNIQUE NOT NULL,
>   created_at  timestamptz DEFAULT now()
> );
>
> projects (
>   id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
>   org_id      uuid NOT NULL REFERENCES organisations(id),
>   name        text NOT NULL,
>   description text,
>   status      text NOT NULL DEFAULT 'active' CHECK (status IN ('active','archived')),
>   created_at  timestamptz DEFAULT now(),
>   updated_at  timestamptz DEFAULT now()
> );
>
> tasks (
>   id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
>   project_id  uuid NOT NULL REFERENCES projects(id),
>   title       text NOT NULL,
>   description text,
>   status      text NOT NULL DEFAULT 'todo' CHECK (status IN ('todo','in_progress','review','done')),
>   assignee_id uuid REFERENCES users(id),
>   priority    int DEFAULT 0,
>   due_date    date,
>   created_at  timestamptz DEFAULT now(),
>   updated_at  timestamptz DEFAULT now()
> );
> -- Denormalised: org_id is NOT on tasks. We join through projects.
> -- Trade-off: simpler schema vs one extra join. At 5M tasks, the join is fine with proper indexing.
>
> comments (
>   id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
>   task_id     uuid NOT NULL REFERENCES tasks(id),
>   author_id   uuid NOT NULL REFERENCES users(id),
>   body        text NOT NULL,
>   created_at  timestamptz DEFAULT now()
> );
>
> task_status_history (
>   id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
>   task_id     uuid NOT NULL REFERENCES tasks(id),
>   old_status  text,
>   new_status  text NOT NULL,
>   changed_by  uuid NOT NULL REFERENCES users(id),
>   changed_at  timestamptz DEFAULT now()
> );
> ```
>
> **Indexes**
> ```sql
> -- Access pattern 1: tasks for a project, filtered by status
> CREATE INDEX idx_tasks_project_status ON tasks (project_id, status);
>
> -- Access pattern 2: comments for a task (ordered by time)
> CREATE INDEX idx_comments_task_created ON comments (task_id, created_at DESC);
>
> -- Access pattern 3: dashboard counts — covered by idx_tasks_project_status
>
> -- Access pattern 4: tasks assigned to a user
> CREATE INDEX idx_tasks_assignee ON tasks (assignee_id) WHERE assignee_id IS NOT NULL;
>
> -- Access pattern 5: status history for a task
> CREATE INDEX idx_status_history_task ON task_status_history (task_id, changed_at DESC);
>
> -- Access pattern 6: text search on tasks
> CREATE INDEX idx_tasks_search ON tasks USING gin (to_tsvector('english', title || ' ' || coalesce(description, '')));
>
> -- Multi-tenant query efficiency
> CREATE INDEX idx_projects_org ON projects (org_id);
> ```
>
> **Trade-offs**
> - **Normalisation vs. query speed:** Status is stored as text on tasks (not a separate statuses table). This denormalises slightly but avoids a join on the most frequent query.
> - **Audit log as separate table:** `task_status_history` is append-only. Could use PostgreSQL's built-in audit triggers instead, but an explicit table is more queryable and portable.
> - **No soft deletes:** Tasks and comments are hard-deleted. If soft deletes are needed later, add a `deleted_at` column and update indexes to exclude deleted rows.
>
> **Evolution Considerations**
> - *Adding subtasks:* Add `parent_task_id` to tasks (self-referential FK). Existing queries unaffected.
> - *Adding labels/tags:* New `task_labels` junction table. Common pattern, low risk.
> - *Scaling beyond 5M tasks:* Partition the tasks table by project_id if query performance degrades. PostgreSQL native partitioning handles this transparently.

## Tuning Notes

- **NoSQL database:** Replace the relational model with document structures optimised for your access patterns. Design around queries, not entities.
- **Event-sourced model:** Replace mutable entities with an event log. The "current state" is derived from replaying events.
- **Greenfield vs. migration:** If migrating from an existing schema, add a "migration plan" section showing how to evolve from old to new without downtime.
- **Review with the team:** Data models benefit enormously from peer review. Share the access patterns first and let the team challenge whether the model serves them well.
