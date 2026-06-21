# Ontology Architecture — Key Decision & Quality Checklist

Use during architecture phases and governance reviews.

## Strategic Alignment
- [ ] Business capabilities and key decisions that need semantic support clearly identified
- [ ] Ontology scope and success criteria expressed in business outcome language
- [ ] Stakeholders and domain experts engaged with clear ownership model

## Architectural Foundations
- [ ] Upper ontology decision documented with rationale (BFO, DOLCE, none, custom, etc.)
- [ ] Layering/modularization strategy defined (core, domain, application, reference ontologies)
- [ ] URI policy, naming conventions, and versioning strategy established
- [ ] Common modeling patterns selected and documented (provenance, temporal, part-whole, quantities, etc.)

## Governance & Operating Model
- [ ] Roles and responsibilities defined (Architect, Developers, Domain Stewards)
- [ ] Change management process documented and socialized
- [ ] Competency question library started for priority domains
- [ ] Deprecation and migration policy defined

## Quality & Fitness
- [ ] Structural quality targets set (consistency, no unwanted inferences, query/reasoning performance)
- [ ] Semantic quality targets set (domain coverage, alignment with reality, fitness for reasoning)
- [ ] Pragmatic quality targets set (usability, adoption, integration effort)
- [ ] Evaluation approach for ontology quality defined (automated + expert review)

## Roadmap & Evolution
- [ ] Prioritized module roadmap aligned with business value and dependencies
- [ ] Incremental delivery approach defined that delivers value early
- [ ] Coexistence/migration strategy for legacy data models and ontologies

## Tooling & Platform
- [ ] Ontology editor, repository, reasoner, and SHACL engine choices made with rationale
- [ ] Integration approach with vector search, relational stores, and document stores defined
- [ ] CI/CD and testing approach for ontologies planned

## Risk & Anti-Pattern Avoidance
- [ ] Monolithic ontology risk assessed and mitigated via modular design
- [ ] Over-modeling risk addressed (reification, complexity)
- [ ] Adoption risk addressed through stakeholder involvement and clear value paths
- [ ] Governance debt risk mitigated with lightweight but clear processes

Revisit this checklist at major architecture milestones and governance reviews. Treat it as a living artifact.
