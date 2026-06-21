# Ontology Architecture Patterns & References

## Foundational Patterns

- **Layered Architecture**: Upper Ontology (optional but powerful for interoperability) → Core / Mid-level Ontologies → Domain Ontologies → Application / Task Ontologies.
- **Modularization**: Design modules with clear boundaries, minimal coupling, and explicit import/dependency management. Enables parallel development and independent evolution.
- **Ontology Design Patterns (ODPs)**: Reusable solutions for common modeling problems (e.g., n-ary relations, provenance, temporal intervals, quantities with units, part-whole). Use established ODPs where they fit.
- **Competency Questions Driven Design**: Every major ontology module should be driven by a set of competency questions that define what the ontology must be able to answer.

## Upper Ontology Considerations
- BFO (Basic Formal Ontology): Excellent for scientific and biomedical domains; strong philosophical grounding and interoperability.
- DOLCE: More cognitive/linguistic orientation.
- Many successful enterprise ontologies use a lightweight or no explicit upper ontology and rely on careful domain modeling + schema.org alignments where helpful.
- Decision criteria: interoperability needs with external systems, reasoning requirements, team familiarity, and long-term maintenance cost.

## Provenance & Trust Patterns (Almost Always Needed)
- PROV-O or lightweight custom provenance modules.
- Attach source, confidence, temporal validity, and authority to key assertions.
- Critical for Ontology-Augmented Generation and any decision-support use case.

## Integration with Modern Data Platforms
- Ontology as semantic layer over data lake/warehouse + vector store.
- Ontology views or virtual graphs over relational data.
- Hybrid retrieval (vector + graph + ontology reasoning) — see Ontology-Augmented Generation skill.

## Governance Anti-Patterns to Avoid
- "Ontology by committee" that produces bloated, unusable models.
- No clear ownership or change process → ontology sprawl and semantic drift.
- Perfect-world modeling disconnected from actual data and usage.
- Treating ontology work as purely technical rather than socio-technical.

## Recommended Further Reading (High Signal)
- Ontology Design Patterns community resources
- BFO documentation and examples (especially in biomedical and enterprise contexts)
- PROV-O and PROV-DM for provenance
- Papers on modular ontology engineering and ontology governance in large organizations

The goal of ontology architecture is not philosophical purity but creating semantic assets that reliably improve decision-making, interoperability, and automation at scale while remaining maintainable over years.
