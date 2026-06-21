---
name: ontology-developer
description: Hands-on implementation of ontologies and knowledge graphs — modeling in OWL/RDF/SHACL/SPARQL/JSON-LD, data mapping and transformation, validation and testing, pipeline integration, tooling, versioning, and deployment of semantic assets — trigger on ontology modeling tasks, SHACL rule development, semantic data pipelines, ontology testing, integration of ontologies into applications or data platforms, or day-to-day ontology engineering work
---

# Ontology Developer

This skill focuses on the practical, hands-on craft of building, testing, integrating, and maintaining ontologies and semantic data assets. Ontology Developers turn architectural designs into working, validated, and integrated semantic components.

## Core Development Lifecycle

1. **Requirements & Competency Questions**
   - Work with domain experts and architects to capture competency questions.
   - Translate business needs into precise ontological commitments (what must be represented and what inferences are required).

2. **Modeling**
   - Choose appropriate formalisms (OWL 2 profiles, RDFS, SHACL, SKOS, etc.).
   - Apply ontology design patterns and follow established naming/URI conventions.
   - Balance expressivity with performance and usability.
   - Document modeling decisions (especially non-obvious ones).

3. **Data Mapping & Population**
   - Design and implement mappings from source data (relational, JSON, CSV, documents) to the ontology.
   - Use R2RML, RML, custom ETL + semantic transformation, or virtual graph approaches.
   - Handle entity resolution, data quality issues, and provenance attachment.

4. **Validation & Testing**
   - Author SHACL shapes for structural and business-rule validation.
   - Use reasoners (HermiT, Pellet, ELK, etc.) for consistency checking and inference testing.
   - Build test suites based on competency questions.
   - Implement automated validation in CI pipelines.

5. **Integration & Deployment**
   - Integrate with application code, APIs, query engines, and agentic systems.
   - Deploy to triple stores, graph databases, or hybrid semantic layers.
   - Version ontologies and manage releases (semantic versioning for ontologies is recommended).

6. **Maintenance & Evolution**
   - Handle ontology changes with minimal disruption (deprecation, migration paths).
   - Monitor usage, performance, and quality metrics.
   - Refactor as understanding deepens or new requirements emerge.

## Recommended Tooling & Stacks

- **Modeling & Editing**: Protégé (desktop), TopBraid Composer, or web-based editors. For code-centric work: text editors + validation scripts.
- **Programming**: Python with `rdflib`, `owlready2`, or `pySHACL`. Java with OWL API or Jena for heavier lifting.
- **Validation**: SHACL (pySHACL, TopBraid SHACL API), reasoners via OWL API or command-line tools.
- **Querying**: SPARQL endpoints (Blazegraph, GraphDB, Stardog, Virtuoso, Amazon Neptune, etc.).
- **Mapping**: RML/R2RML engines, custom Python transformation pipelines, or virtual graph technologies.
- **Versioning & CI**: Git + ontology diff tools + automated validation in CI/CD pipelines.
- **Observability**: Query logging, usage analytics on the semantic layer, performance monitoring.

## Key Technical Practices

- **Start lightweight**: Begin with RDFS + SKOS + simple OWL where possible. Add expressivity only when needed for reasoning or validation.
- **SHACL-first validation**: Use SHACL for most business rules and data quality constraints — it is more maintainable and performant than heavy OWL axioms for many use cases.
- **Provenance by default**: Attach source, timestamp, confidence, and authority to important assertions.
- **Test-driven ontology development**: Write competency questions and SHACL shapes before or alongside modeling.
- **Performance awareness**: Understand the reasoning profile (EL, QL, RL, DL) and its implications. Profile queries and inferences on realistic data volumes.
- **Hybrid architectures**: Most production systems combine ontologies with vector search, relational data, and documents. Design the ontology to complement rather than replace other paradigms.

## Common Pitfalls & How to Avoid Them

- Over-modeling with complex OWL axioms that are rarely used and hurt performance.
- Writing SHACL shapes that are too loose (miss real errors) or too brittle (break on minor data variations).
- Poor entity resolution and duplicate handling during data mapping.
- Ignoring versioning and deprecation — leads to breaking changes for consumers.
- Building ontologies in isolation from the applications and agents that will consume them.
- Under-investing in documentation and examples for other developers.

## Integration Points with Other Skills

- Work under the guidance of `ontology-architect` for large-scale or governed work.
- Support `forward-deployed-engineer` by rapidly building and iterating ontology modules during customer deployments.
- Enable `ontology-augmented-generation` by producing high-quality, validated ontologies ready for prompt injection and grounded retrieval.
- In `skunkworks-agent-coder` contexts, provide lightweight, fast-turnaround ontology support without heavy governance.

## Measurement of Good Ontology Developer Work

- Ontologies that pass automated validation and competency question tests.
- Low time from requirement to deployed, queryable semantic asset.
- High adoption and low friction for downstream consumers (applications, agents, analysts).
- Clean evolution history with minimal breaking changes.
- Clear documentation and examples that allow others to extend or use the ontology effectively.

The best Ontology Developers combine deep technical skill with pragmatism — they deliver semantic assets that are correct enough, fast enough, and useful enough for real operational impact.