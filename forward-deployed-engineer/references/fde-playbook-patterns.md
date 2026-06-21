# Forward Deployed Engineer Playbook Patterns (Senior/Chief)

## The "Ontology-First Deployment" Pattern
Start every engagement by treating the customer's ontology (or the need to build one) as the central artifact. 
- Map existing data models to ontology concepts early.
- Any new capability must be expressible in ontological terms before heavy implementation.
- This creates natural alignment between data, logic, actions, and user workflows.

## The "Embedded Value Team" Pattern
FDE + 1–2 customer power users + minimal platform support = maximum speed.
- Power users become ontology co-owners and internal champions.
- Daily standups with operators, weekly sync with product/ontology architects.
- You facilitate; they own the operational outcome.

## The "80/20 Ontology Slice" Pattern
Never build the perfect enterprise ontology in the first deployment.
- Identify the 10–20% of classes/relations that cover 80% of the target workflow pain.
- Build a focused application ontology or ontology module.
- Design for later merging into broader enterprise ontology (use modular patterns, upper ontology alignment where possible).

## The "Provenance by Default" Pattern
Instrument every data flow, transformation, inference, and action with lineage from the first prototype.
- Use ontology properties for provenance where possible.
- This single habit dramatically increases trust and reduces debugging time in complex environments.

## The "Feedback as Product Asset" Pattern
Treat every piece of customer feedback as a high-value product input.
- Capture it structured (problem, ontology impact, suggested improvement, business value).
- Quantify where possible.
- Present it in product-friendly formats (not raw complaints).

## Common Senior FDE Anti-Patterns
- Acting as a traditional consultant who writes reports instead of shipping working ontology-grounded capabilities.
- Over-committing to scope that requires perfect data or perfect ontology.
- Building shadow systems outside the customer's ontology/platform.
- Failing to build customer ontology and platform ownership early.
- Optimizing for demo beauty instead of operational friction reduction.

## When to Bring in Ontology Architect vs Ontology Developer
- **Ontology Architect**: Large-scale governance, enterprise ontology strategy, complex modular design, upper ontology decisions, long-term roadmap.
- **Ontology Developer**: Hands-on modeling, SHACL rules, data mapping pipelines, validation suites, performance tuning, day-to-day ontology changes during deployment.

Use the dedicated skills for deeper dives when the deployment hits these areas.

These patterns have been refined across many successful high-stakes deployments in complex data and AI platform environments.
