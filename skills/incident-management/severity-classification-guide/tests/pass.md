**Incident Severity Classification Guide**

*Rule of thumb: classify based on customer impact, not technical complexity.*

**P0 — Critical**
| Field | Value |
|-------|-------|
| Examples | Full outage; checkout down; data loss |
| Acknowledge | 5 minutes |
| Target resolution | 1 hour |
| Communication | Status page + exec channel, every 30 min |

**P1 — Major**
| Field | Value |
|-------|-------|
| Acknowledge | 15 minutes |
| Target resolution | 4 hours |
| Communication | Incident channel, hourly |

**P2 — Minor**
| Field | Value |
|-------|-------|
| Acknowledge | 1 hour |
| Target resolution | 2 days |
| Communication | Ticket update |

**P3 — Low**
| Field | Value |
|-------|-------|
| Acknowledge | next business day |
| Target resolution | backlog |
| Communication | Ticket only |

**Quick Classification Flowchart**
Is the whole product down? → YES → P0.
