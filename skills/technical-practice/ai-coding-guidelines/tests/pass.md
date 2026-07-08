**Platform Team — AI-Assisted Coding Guidelines**

**Stance:** AI assistants are encouraged. The engineer who merges the code owns it — correctness, security, and licensing.

**When to use / when to be careful**
- Good fit: boilerplate, tests, refactors, unfamiliar syntax, exploring an API.
- Extra scrutiny: auth, cryptography, payment paths, novel algorithms, anything touching regulated data.

**Review & verification bar**
- AI-generated code is reviewed to the same standard as any code. The author must understand every line they submit and must run and test it — never merge on faith.

**Secrets & data**
- Never paste: secrets, keys, customer PII, or proprietary source into a non-approved tool.
- Approved tools/settings: enterprise-plan assistants with training-opt-out enabled.

**Security**
- Treat generated code as untrusted input: check for insecure defaults and injected flaws, and verify any suggested dependency actually exists and is maintained before adding it.

**Licensing & attribution**
- Generated code can resemble licensed sources. Flag anything that looks copied for review; legal confirms provenance handling.

**Accountability**
- The submitting engineer is responsible regardless of how the code was produced. "The AI wrote it" is never an excuse for a defect. AI assistance need not be disclosed per-commit, but must be if a reviewer asks.
