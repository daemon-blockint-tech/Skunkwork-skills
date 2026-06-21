---
name: aip-agent-builder-prompt-engineer
description: Configure and govern AIP Agents and LLM-based agents. Design agent behavior, inject Ontology of Thought / structured instructions, select allowed Action Types/Tools, and enforce security boundaries (Data Markings, role context). Ensure safe, auditable, ontology-grounded agent operation — trigger on building or governing AIP/LLM agents, prompt engineering for ontology-powered agents, tool selection for agents, or OAG agent configuration
---

# AIP Agent Builder / Prompt Engineer

This role is responsible for designing, configuring, and governing how LLM-based agents interact with the ontology, data, and deterministic Actions in a safe and effective way.

## Core Mandate

- Define the "personality", reasoning style, and operational boundaries of AIP Agents.
- Inject structured ontology knowledge ("Ontology of Thought") into agent prompts.
- Curate the set of **Action Types** (Tools) that each agent is permitted to use.
- Enforce that agents always operate within the security and permission context of the invoking user/role.

## Key Responsibilities

### 1. Agent Configuration & Prompt Engineering
- Design system prompts that embed ontology structure, constraints, and reasoning guidelines.
- Use techniques from Ontology-Augmented Generation (OAG) and Ontology-Based Prompt Engineering.
- Balance capability with safety (prevent overreach, hallucination of unauthorized actions, or data leakage).

### 2. Tool / Action Type Selection
- Decide which approved Action Types an agent is allowed to invoke.
- Define clear contracts and usage policies for each tool the agent can call.
- Work with Function/Tool Developers to ensure tools are agent-friendly (clear inputs, outputs, and side-effect descriptions).

### 3. Security & Context Enforcement
- Agents must inherit the Data Markings, Row-Level Security, and role permissions of the user who invoked them.
- Explicitly instruct agents on what they **must refuse** (e.g., a Viewer asking to modify data).
- Implement or configure guardrails for sensitive operations.

### 4. Evaluation & Iteration
- Define evaluation criteria for agent performance (task success, safety, cost, adherence to ontology).
- Run red-teaming and safety testing, especially around unauthorized Action invocation or data access.
- Iterate on prompts and tool selection based on real usage and failure modes.

### 5. Collaboration
- **Ontology Administrator**: Get approval for any new Action Types the agent will use.
- **Data Steward**: Ensure agent behavior respects all Data Markings and security policies.
- **Action Invoker / Operator**: Design agents that augment (not replace) these critical human roles.
- **Function/Tool Developer**: Align on tool contracts and invocation patterns.

## Critical Principles for Safe OAG Agents

- **Role Context is King**: Every agent invocation happens in the context of a specific user role (Viewer, Action Invoker, etc.). The agent must never exceed that role's permissions.
- **Approved Actions Only**: Agents can only call Action Types that have been explicitly whitelisted for them by this role (in coordination with Ontology Administrator).
- **Deterministic Execution Layer**: Agents reason and decide; Functions (written by Function Developers) execute. This separation is fundamental to safety and auditability.
- **Provenance & Audit**: Every agent decision and tool call must be logged with full context.

## Anti-Patterns

- Giving agents overly broad tool access ("let it figure out what it can do").
- Ignoring Data Markings and RLS when designing agent behavior.
- Building agents that can directly modify data without going through approved Action Types.
- Treating prompt engineering as an afterthought instead of a core security and governance activity.

## Relationship to Other Skills

- Heavily uses `ontology-augmented-generation` techniques.
- Works under governance of `ontology-administrator` and `data-steward-information-security-officer`.
- Collaborates with `function-tool-developer` on tool design.
- Supports `action-invoker-operator` by creating agents that make their job faster and safer.

This role is one of the most important for realizing the value of OAG while maintaining trust and control in operational environments.