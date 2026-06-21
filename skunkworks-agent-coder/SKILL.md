---
name: skunkworks-agent-coder
description: Apply Skunkworks methodology to the rapid development of AI agents, coding agents, and agentic systems — small autonomous high-trust teams, radical iteration speed, minimal bureaucracy, direct problem ownership, fail-fast experimentation, and 80/20 delivery — trigger on building agents quickly, skunkworks-style agent projects, autonomous coding workflows, or when standard agile/process-heavy approaches are too slow for agentic innovation
---

# Skunkworks Methodology for Agent Coder / Agentic Development

This skill adapts the legendary Lockheed Skunkworks model (small elite team, radical autonomy, minimal process, extreme ownership, rapid results) to the domain of building AI agents, coding agents, multi-agent systems, and agentic workflows.

The core premise: In fast-moving agentic AI, traditional agile, heavy governance, or large-team coordination often kills the speed and creativity required. Skunkworks mode trades process for velocity, trust, and direct accountability.

## Core Skunkworks Principles (Adapted for Agents)

1. **Small, elite, autonomous team**
   - Ideal: 3–8 highly capable people (mix of agent architects, prompt/system engineers, evaluators, domain experts).
   - Maximum autonomy from bureaucracy, approval chains, and unnecessary coordination.
   - One clear technical lead with final say on architecture and scope.

2. **Radical ownership & direct problem connection**
   - The team owns the problem end-to-end (not just "build to spec").
   - Direct access to real users, real data, real operational context (or the closest possible proxy).
   - No handoffs. The people who understand the problem build the solution.

3. **80/20 and "good enough to ship" mindset**
   - Deliver working agent capabilities that solve real problems in days to low weeks.
   - Perfect architecture and comprehensive testing come later (or never, if the agent is replaced by something better).
   - Bias toward shipping and learning over planning and documenting.

4. **Fail fast, learn faster, iterate ruthlessly**
   - Build the smallest possible agent that can demonstrate value or disprove an assumption.
   - Instrument heavy evaluation from day one (task success rate, cost, latency, human preference, failure modes).
   - Kill or pivot ideas quickly when data shows they don't work.

5. **Minimal viable process**
   - Daily standups only if they add value (often async + weekly deep sync is enough).
   - Documentation is minimal and living (architecture decision records for key choices, runbooks for critical paths).
   - Tooling and infrastructure are chosen for speed, not standardization (unless the output must run in production).

6. **High trust, high accountability**
   - Trust is given upfront. Accountability is on results, not process compliance.
   - Psychological safety to experiment and admit failure early.
   - Credit is shared; blame is avoided.

## Recommended Operating Cadence for Agent Skunkworks

- **Day 0–2: Problem framing & hypothesis**
  - Define the exact agent capability or workflow to build.
  - Write 3–5 crisp success criteria + failure criteria.
  - Choose evaluation approach (human eval, LLM-as-judge, task completion rate, cost/latency budgets).

- **Day 2–7: First working prototype**
  - Build the thinnest possible agent (single agent + tools or simple multi-agent).
  - Use the simplest viable architecture (ReAct, tool-calling, basic planning, or even scripted orchestration if it works).
  - Heavy instrumentation and logging.

- **Day 7–14: Ruthless iteration**
  - Run evaluation harness continuously.
  - Identify top failure modes and fix the highest-leverage ones.
  - Add complexity (memory, multi-agent collaboration, better tools, self-critique) only when it moves the success metrics.

- **Day 14–30: Hardening & transition (if keeping)**
  - If the agent shows sustained value, begin hardening (error handling, monitoring, cost control, production deployment).
  - Document key decisions and create minimal runbooks.
  - Decide: productionize, hand off to another team, or archive and move to next problem.

## When Skunkworks Mode is Appropriate (and When It Is Not)

**Use Skunkworks when:**
- The problem is novel or poorly understood.
- Speed of learning matters more than process compliance.
- You have (or can assemble) a small team of high-caliber people with domain + agent expertise.
- The organization can tolerate (and protect) a high-autonomy pocket.
- You need to explore agentic patterns that standard teams would over-engineer or under-explore.

**Avoid or transition out when:**
- The agent must meet strict regulatory, security, or reliability requirements from day one.
- Large-scale coordination across many teams is required.
- The solution needs to be maintained long-term by a larger organization (plan transition early).
- Political or budgetary constraints make true autonomy impossible.

## Anti-Patterns in Agent Skunkworks

- Pretending to be in Skunkworks while still running heavy process underneath.
- Building agents in isolation without real user/data feedback loops.
- Over-investing in beautiful multi-agent frameworks before validating basic single-agent performance.
- Ignoring evaluation and cost/latency until "later".
- Using Skunkworks as an excuse for poor engineering hygiene on things that do matter (security, basic monitoring, reproducibility).
- Scaling the team too early (Skunkworks dies with headcount bloat).

## Tooling & Infrastructure Recommendations (Speed First)

- Choose agent frameworks and tooling that let you move fastest (LangGraph, CrewAI, AutoGen, custom lightweight orchestrators, or even direct LLM tool-calling loops).
- Evaluation harness is non-negotiable — build or adapt one early (task datasets, LLM judges, human eval pipelines).
- Observability: LangSmith, Phoenix, Helicone, or custom logging + dashboards from the start.
- Versioning: Git + clear experiment tracking (prompts, agent configs, tool definitions).

## Relationship to Other Skills

- Combine with `ontology-augmented-generation` or `ontology-developer` when agents must be ontology-grounded.
- Use `forward-deployed-engineer` patterns when the skunkworks output needs to be deployed inside a customer environment.
- For large-scale ontology work that supports many agents, bring in `ontology-architect`.

Skunkworks is not chaos. It is disciplined autonomy focused on the fastest possible path from problem to validated agentic solution. The best agent skunkworks teams ship remarkable capabilities while larger organizations are still writing requirements documents.