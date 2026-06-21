# Action Type Governance Checklist (For Ontology Administrator)

Use this checklist whenever a new Action Type is proposed or an existing one is modified.

## 1. Business & Operational Justification
- [ ] Clear operational problem this Action solves
- [ ] Quantified or qualified value (time saved, risk reduced, decision improved)
- [ ] Alignment with domain priorities (defense, logistics, health, etc.)

## 2. Schema & Ontology Alignment
- [ ] Action Type name follows established naming conventions
- [ ] Input and output types are existing Object Types or well-defined primitives
- [ ] Side effects on Object Types / Links are explicitly documented
- [ ] Ontology Administrator has reviewed and approved the semantic definition

## 3. Security & Data Markings
- [ ] Required minimum Data Marking / clearance level to invoke
- [ ] Row-Level or Object-Level Security rules that apply
- [ ] Does the Action respect or enforce Data Markings on affected objects?
- [ ] Data Steward / Information Security Officer has reviewed security implications

## 4. Deterministic Implementation (Function/Tool Developer)
- [ ] Implemented in approved language (TypeScript / Python / Rust)
- [ ] Idempotency characteristics clearly documented
- [ ] Error handling and failure modes defined
- [ ] Full audit logging and provenance capture implemented
- [ ] Unit + integration tests passing with realistic data

## 5. Agent & Human Usability
- [ ] Clear description suitable for LLM tool selection / prompting
- [ ] Input parameters well-documented with examples
- [ ] Output format structured and easy for agents to consume
- [ ] AIP Agent Builder has reviewed for agent-friendliness

## 6. Governance & Lifecycle
- [ ] Owner assigned (person or team)
- [ ] Version number assigned
- [ ] Deprecation policy defined (if replacing an older Action)
- [ ] Approval recorded by Ontology Administrator
- [ ] Communication plan to affected roles (Action Invokers, Agent Builders, etc.)

## 7. Testing & Safety
- [ ] Tested in non-production environment with representative users/agents
- [ ] Red-team tested for potential misuse or security bypass
- [ ] Rollback plan defined

Only after all relevant items are checked and signed off should the Action Type be promoted to production and made available to AIP Agents and authorized human roles.

This checklist ensures that every Action Type is safe, governed, and ready for both human operators and AI agents in high-stakes environments.
