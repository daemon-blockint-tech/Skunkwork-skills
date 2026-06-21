# Key Concepts, Papers, and References for Ontology-Augmented Generation

## Core Distinctions

- **Standard RAG**: Retrieves unstructured text chunks via vector similarity → LLM synthesizes. Prone to hallucination, context dilution, and semantic drift.
- **Ontology-Grounded RAG (OG-RAG)**: Anchors retrieval and generation in a formal ontology (classes, relations, axioms). Uses hypergraphs or ontology traversals for retrieval. Improves factual precision and enables verification.
- **Ontology-Augmented Generation (OAG)**: Broader enterprise term (popularized by Palantir AIP). Goes beyond retrieval to include:
  - Typed data objects from governed ontology
  - Deterministic logic (calculations, rules, ML models exposed as functions)
  - Actions (workflows that update source systems)
  - Full provenance and auditability
  - Decision-centric loop: LLM plans → deterministic execution → LLM synthesizes final output
- **Ontology-Based Prompt Engineering**: Injects ontology definitions, constraints, and examples directly into prompts (few-shot or zero-shot) to guide structured generation, query synthesis (text-to-SPARQL), or constrained output without external retrieval. Often combined with the above.

## Recommended Reading & Summaries

### OG-RAG: Ontology-Grounded Retrieval-Augmented Generation (Sharma et al., 2024/2025)
- arXiv:2412.15235 / EMNLP 2025
- Key idea: Build a hypergraph where hyperedges represent clusters of factual knowledge explicitly grounded in domain ontology concepts and relations.
- Retrieval operates over hyperedges rather than flat chunks → better coverage of relational and multi-hop queries.
- Improves LLM responses on domain-specific, complex questions by reducing ungrounded generation.
- Implementation notes: Requires ontology + document corpus → hypergraph construction step (can be LLM-assisted or rule-based). Hybrid vector + graph retrieval.

### Palantir Ontology Augmented Generation (OAG)
- Core of Palantir AIP / Foundry.
- Enterprise ontology = single source of truth containing:
  - Objects (typed entities with properties, links/relations)
  - Logic (Python transforms, ML models, optimizers, forecasts — exposed as callable)
  - Actions (templated workflows with approval gates that mutate operational systems)
- LLM never directly mutates data; it interacts via the ontology layer.
- Benefits demonstrated: dramatically lower hallucination rates, full lineage/provenance, ability to "show its work" with live data + deterministic steps, trust in regulated/operational environments.
- Pattern: Ontology navigation (search typed objects) → LLM proposes plan or partial answer → invoke logic/actions deterministically → feed typed results back → final grounded synthesis.

### Ontology-Based Prompt Engineering (various 2025 papers)
- Examples: Text-to-SPARQL generation in health domain; improving structured output fidelity.
- Technique: Include ontology excerpt (classes + properties + constraints) + positive/negative examples in the prompt.
- Particularly effective for:
  - Generating valid queries against a schema/ontology
  - Producing JSON or RDF that conforms to an ontology
  - Reducing invalid or invented terminology in specialized domains
- Works well even without retrieval when the ontology itself encodes most of the needed domain knowledge.

## Practical Ontology Serialization Examples

See assets/prompt-templates.md for the recommended compact formats.

Additional patterns:
- **Minimal Viable Ontology (MVO)**: For a new domain, define only the 5–15 classes and 10–20 relations/properties most relevant to the target tasks. Expand later based on verification failures.
- **Modular Injection**: Maintain multiple small ontology modules (e.g., core entities, constraints, actions) and load only the needed subset per prompt.
- **Hybrid Text + Structured**: Combine natural language descriptions of axioms with a machine-readable JSON Schema for the same concepts. LLM uses NL for reasoning; downstream systems use schema for validation.

## Common Failure Modes & Mitigations (from literature + practice)

1. **Ontology too large** → Context dilution, lost signal. Mitigation: Curate task-specific views or use retrieval over ontology itself.
2. **LLM ignores constraints** → Especially in long contexts. Mitigation: Strong system rules + few-shot examples that demonstrate enforcement + post-generation verification step.
3. **Missing inference support** → Ontology only has schema, not rules. Mitigation: Either (a) add SWRL-like rules or Python logic to ontology, or (b) instruct LLM to perform explicit inference steps with justification.
4. **Stale ontology** → Generation uses outdated constraints. Mitigation: Version ontologies; include ontology version/timestamp in every prompt; refresh from source before critical tasks.
5. **Verification overhead** → Extra tokens/calls. Mitigation: Make verification lightweight (targeted LLM judge or simple rule scripts); cache common checks; apply only on high-stakes outputs.

## Tooling Recommendations (General, not Palantir-specific)

- Python: rdflib or owlready2 for parsing OWL/RDF (if available in env); or treat ontology as JSON/YAML dict for lightweight cases.
- Validation: jsonschema for JSON outputs; custom Python rules for cardinality/relation checks.
- Visualization: Mermaid or Graphviz for ontology diagrams (include rendered version or source in prompt).
- Storage: Keep canonical ontology in Turtle/JSON-LD + versioned snapshots used in prompts.

This reference document should be loaded when deeper background or alternative patterns are needed. For day-to-day use, the SKILL.md workflow + prompt templates in assets/ are usually sufficient.
