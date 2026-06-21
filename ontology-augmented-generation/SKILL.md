---
name: ontology-augmented-generation
description: Apply Ontology-Augmented Generation (OAG), Ontology-Grounded RAG (OG-RAG), or Ontology-Based Prompt Engineering to ground LLM responses in formal domain ontologies for higher factual accuracy, lower hallucinations, structured outputs and explainable reasoning — use for domain-specific reliable generation, enterprise decision workflows, text-to-SPARQL/SQL/Cypher tasks, hypergraph retrieval setups, or when vector RAG or plain prompting fails to enforce semantic consistency and domain constraints
---

# Ontology-Augmented Generation and Ontology-Based Prompt Engineering

Use this skill to produce more reliable, semantically grounded outputs by systematically incorporating ontologies into prompts, retrieval, and verification loops. Ontologies here mean formal or semi-formal models defining classes, properties, relations, constraints, and (where possible) rules or actions.

## Core Workflow (Follow in Order)

1. **Identify or Construct Relevant Ontology**
   - Start with existing standards (schema.org, Dublin Core, domain ontologies like FIBO for finance, SNOMED CT or Mondo for biomed, or custom).
   - If none exists, bootstrap: Extract candidate classes/relations from source documents or data using LLM, then manually or iteratively refine into a minimal viable ontology (focus on 10-30 core concepts + key relations first).
   - Represent as OWL/RDF, JSON-LD, or simple property graph schema. Store source in references/ or assets/ for reuse.
   - Curate a task-specific subset — never dump an entire large ontology into context.

2. **Serialize Ontology into Prompt-Friendly Form**
   - Preferred compact formats (choose based on token budget and task):
     - Hierarchical indented text: Class hierarchies with `subClassOf`, key `properties`, `relations` (domain/range), cardinalities, and example instances.
     - JSON Schema or JSON-LD snippet focused on relevant classes/properties.
     - Natural language glossary + axiom list (e.g., "Every `Order` must have exactly one `customer` and at least one `item`").
     - Visual aids: Mermaid class diagram or ER diagram (include in prompt or as separate asset).
   - Explicitly list disallowed or constrained elements to reduce hallucination surface.
   - Example serialization structure (adapt and place in prompt):
     ```
     ## Domain Ontology: E-Commerce
     Classes:
     - Product (properties: name, price, category, inStock: boolean)
     - Order (properties: orderId, date, status)
     - Customer (properties: id, name, tier)
     Relations:
     - places (Customer -> Order, 1:*)
     - contains (Order -> Product, 1:* , with quantity)
     Constraints/Axioms:
     - Order.status in {pending, shipped, delivered, cancelled}
     - Product.price > 0
     - ...
     ```

3. **Craft Ontology-Grounded System + Few-Shot Prompts**
   - System instruction template:
     "You are a precise [domain] reasoning engine. You MUST ground every assertion, classification, relation, or recommendation strictly in the provided ontology. Never invent classes, properties, or relations outside the ontology. If information is missing or inference is required, state the ontological basis or note the gap. Output in the requested format and cite specific ontology elements used."
   - Append the serialized ontology.
   - Add 2–4 few-shot examples. Each example must:
     - Show user input.
     - Demonstrate explicit use of ontology elements in reasoning or output.
     - Include a short "Ontology trace" or justification.
   - For output control: Specify JSON conforming to ontology classes, or natural language with inline ontology references (e.g., `[Product: SKU-123]`), or both.
   - For query generation tasks (text-to-SPARQL etc.): Include ontology + target query language schema; instruct LLM to produce queries that are valid w.r.t. the ontology.

4. **Ontology-Grounded Retrieval (OG-RAG Style)**
   - Pre-process corpus: Annotate or cluster documents into hyperedges linked by ontology concepts/relations (e.g., all facts about a specific `Patient` instance or `ClinicalTrial` linked via `treats` relation).
   - Retrieval strategy (hybrid):
     - Vector search on chunks.
     - Ontology-aware expansion: Traverse ontology relations from query entities to pull related context.
     - Hypergraph retrieval: Score and select hyperedges that best cover query concepts and relations.
   - Post-retrieval filter: Discard or down-rank items that violate ontology constraints (type mismatches, etc.).
   - In prompt: Present retrieved items with their ontological types/relations highlighted.

5. **Generation + Verification Loop (Critical for Reliability)**
   - Generate initial response using the grounded prompt.
   - Verify:
     - Syntactic/structural: Output parses against expected schema (JSON Schema validation via script or LLM).
     - Semantic/ontology: Check for undefined terms, violated cardinalities, disallowed relations, or contradictions with axioms. Use LLM self-critique ("List every ontology element referenced and confirm adherence") or lightweight rule checker.
     - If violations found: Either (a) iterate generation with explicit correction instructions, or (b) surface the issue with provenance.
   - Provenance: Always include source ontology elements, retrieved hyperedges, or invoked logic/actions that contributed to the final output.
   - For decision-centric OAG (enterprise style): Model logic (calculations, forecasts, rules) and actions (approvals, API calls, updates) as first-class ontology citizens. LLM proposes plan → execute deterministic steps via tools → feed typed results back into context for final synthesis.

6. **Output Formats and Tooling**
   - Prefer structured outputs (JSON-LD, RDF, typed objects) over free text when possible — easier to validate and consume downstream.
   - When live data or actions are involved, expose them as ontology-grounded tools/functions the LLM can "call" (ReAct-style or native function calling with ontology types).
   - Track full lineage: ontology version + retrieval ids + tool calls + generation timestamp.

## Best Practices and Anti-Patterns

- Keep ontology injection focused and modular — large ontologies cause context dilution.
- Combine with standard techniques: chain-of-thought, self-consistency, or tree-of-thoughts, but always ontology-constrained.
- For Palantir-style OAG: Emphasize the Ontology as the single source of truth containing data objects + logic + actions. Ground every LLM step in live ontology queries and deterministic execution rather than pure generation.
- Avoid: Treating ontology as mere "extra context" without enforcement; ignoring constraints during generation; failing to verify outputs.
- Scale: Start with narrow scoped ontology for a specific workflow; expand iteratively based on failure modes observed in verification.

## Resources in This Skill

- `references/`: Detailed examples, paper summaries (OG-RAG, Palantir OAG), serialization templates, full sample ontologies (Turtle/JSON-LD), and domain-specific patterns.
- `assets/`: Reusable prompt template files (system prompts, few-shot packs, verification checklists) that you can copy and adapt directly into responses.
- `scripts/`: Helper Python scripts for ontology serialization, basic validation against simple schemas, hypergraph construction stubs, or converting common formats (JSON Schema ↔ text). Run via `python scripts/<name>.py` when needed for deterministic processing. Install any required pure-Python deps if missing in the environment (prefer stdlib + minimal).

## Iteration Guidance

After using this skill on a task:
- Capture recurring failure modes (e.g., specific relation hallucinations) and strengthen the ontology or add verification rules.
- Refine serialization format based on token usage vs. accuracy trade-off.
- Version the ontology and prompt templates together.

This skill turns ad-hoc prompting into a repeatable, auditable engineering discipline centered on explicit semantics.