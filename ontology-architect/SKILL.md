---
name: ontology-architect
description: Design enterprise-scale ontologies, knowledge graphs, and semantic architectures — strategic modeling, governance frameworks, modular patterns, business capability alignment, semantic interoperability, and long-term ontology roadmaps — trigger on enterprise ontology strategy, knowledge graph architecture, ontology governance, large-scale semantic modeling, upper ontology decisions, or when ontology work requires architectural thinking beyond implementation
---

# Ontology Architect

This skill captures the strategic and architectural discipline of designing, governing, and evolving ontologies and knowledge graph platforms at enterprise scale. An Ontology Architect operates at the intersection of business strategy, data architecture, and semantic technology.

## Core Responsibilities of an Ontology Architect

- Define the **ontology strategy** aligned with business capabilities and data strategy.
- Establish **governance** (ownership, change processes, quality standards, deprecation policies).
- Design **modular ontology architecture** (upper ontologies, domain ontologies, application ontologies, ontology patterns).
- Ensure **semantic interoperability** across systems, domains, and external partners.
- Create **roadmaps** for ontology evolution that balance short-term delivery with long-term coherence.
- Define **quality and fitness-for-purpose** metrics and evaluation frameworks.
- Advise on **tooling and platform choices** for the semantic layer (triple stores, graph databases, ontology editors, reasoners, SHACL engines, etc.).

## Ontology Architecture Process (Repeatable)

1. **Business & Capability Alignment**
   - Map key business capabilities and decision-making processes.
   - Identify where semantic precision, interoperability, or reasoning will create the highest leverage.
   - Define ontology scope boundaries and success criteria in business terms.

2. **Current-State Semantic Assessment**
   - Inventory existing data models, taxonomies, ontologies, and semantic assets.
   - Assess quality, coverage, consistency, and fitness for intended uses.
   - Identify integration points and semantic conflicts.

3. **Target Ontology Architecture Design**
   - Choose upper ontology foundation (BFO, DOLCE, schema.org extensions, custom, or none).
   - Define ontology layers/modules and their relationships (core, domain, application, reference).
   - Establish naming, URI, versioning, and modularization conventions.
   - Design patterns for common modeling situations (part-whole, provenance, temporal, quantities, etc.).

4. **Governance & Operating Model**
   - Define roles (Ontology Architect, Ontology Developer, Domain Stewards, Data Stewards).
   - Establish change management processes (proposal → review → approval → deployment).
   - Create competency question libraries and test suites that drive design and validation.
   - Set policies for ontology publication, deprecation, and external alignment.

5. **Roadmap & Evolution Planning**
   - Prioritize ontology modules by business value and dependency.
   - Plan incremental delivery that delivers value while maintaining coherence.
   - Define migration and coexistence strategies for legacy models.

6. **Quality Framework**
   - Structural quality (consistency, no unintended inferences, performance).
   - Semantic quality (coverage of domain, alignment with reality, fitness for reasoning tasks).
   - Pragmatic quality (usability by developers and applications, adoption).
   - Governance quality (compliance with processes, documentation, ownership clarity).

## Key Architectural Patterns & Decisions

- **Upper vs Domain vs Application Ontologies**: Use upper ontologies sparingly and only where they add real value. Most operational value comes from well-designed domain and application ontologies.
- **Modularization**: Design for reuse and independent evolution. Use ontology imports, views, and layering.
- **Provenance & Trust**: Almost every enterprise ontology needs strong patterns for source, confidence, temporal validity, and authority.
- **Reasoning Scope**: Decide explicitly what reasoning will be done at ontology level vs application level vs data pipeline level.
- **Hybrid Architectures**: Most successful enterprise deployments combine ontologies with vector search, relational data, and document stores (see Ontology-Augmented Generation skill).

## Common Anti-Patterns

- Building a single monolithic "enterprise ontology" that tries to model everything.
- Choosing an upper ontology for philosophical purity rather than practical utility.
- Designing beautiful ontologies with no clear path to operational use or application integration.
- Under-investing in governance and change management (leads to ontology sprawl and inconsistency).
- Ignoring the socio-technical aspects (stakeholder alignment, domain expert involvement, adoption incentives).
- Over-modeling (excessive reification, unnecessary complexity) that harms usability and performance.

## When to Engage Ontology Architect vs Ontology Developer

- **Ontology Architect**: Strategy, governance, large-scale modular design, upper ontology choices, enterprise roadmap, cross-domain alignment, platform architecture.
- **Ontology Developer**: Hands-on modeling, SHACL implementation, data mapping, validation rule authoring, pipeline integration, day-to-day changes, performance tuning.

The best Ontology Architects spend significant time with Ontology Developers and domain experts to keep architecture grounded in implementable reality.

## Integration with Other Skills

- Works closely with `ontology-developer` for implementation.
- Supports `forward-deployed-engineer` deployments with sound architectural foundations.
- Enables advanced `ontology-augmented-generation` and agentic systems that require reliable semantic grounding.
- In Skunkworks contexts, provide lightweight architectural guardrails without slowing velocity.

Mastery of this skill means creating ontologies that are simultaneously strategically coherent, technically sound, and operationally valuable — and that improve over time rather than accumulate technical debt.