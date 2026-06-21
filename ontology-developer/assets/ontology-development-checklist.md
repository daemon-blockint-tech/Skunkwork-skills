# Ontology Developer — Practical Development Checklist

Use for day-to-day ontology work and project kickoffs.

## Requirements & Scoping
- [ ] Competency questions captured and prioritized with domain experts
- [ ] Scope of ontology module clearly bounded
- [ ] Existing related ontologies or data models reviewed for reuse/alignment

## Modeling
- [ ] Appropriate formalism chosen (RDFS + SKOS, OWL 2 EL/QL/RL/DL profile)
- [ ] Ontology design patterns applied where relevant
- [ ] Naming, URI, and modularization conventions followed
- [ ] Key modeling decisions documented (ADR style for non-obvious choices)
- [ ] Initial consistency checked with reasoner

## Validation & Testing
- [ ] SHACL shapes written for structural and business constraints
- [ ] Test data created that exercises competency questions
- [ ] Automated validation suite passing (SHACL + reasoner)
- [ ] Edge cases and negative tests included

## Data Mapping & Population
- [ ] Mapping approach defined (RML, custom ETL, virtual graphs, etc.)
- [ ] Entity resolution and deduplication strategy implemented
- [ ] Provenance attachment implemented for key assertions
- [ ] Sample data loaded and validated end-to-end

## Integration & Deployment
- [ ] SPARQL queries or API access tested with realistic workloads
- [ ] Integration with downstream applications/agents validated
- [ ] Versioning and release process followed
- [ ] Documentation and examples published for consumers

## Maintenance & Evolution
- [ ] Deprecation policy applied for any removed/changed elements
- [ ] Migration path provided for breaking changes
- [ ] Usage metrics and query performance monitored
- [ ] Feedback loop with consumers established

Treat this as a living checklist. Add project-specific items as needed.
