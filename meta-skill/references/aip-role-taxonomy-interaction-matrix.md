# AIP Role Taxonomy & Interaction Matrix (Generalizable to Defense, Logistics, Health, etc.)

This document defines a coherent role taxonomy for ontology-powered AI platforms (inspired by Palantir AIP but designed for general use across defense, logistics, healthcare, manufacturing, and other domains). It emphasizes clear separation of concerns, security boundaries (Data Markings), and safe AI interaction via Ontology + Actions + OAG.

## Core Principles

- **Least Privilege & Clear Boundaries**: Every role has the minimum permissions needed. AI agents inherit the same restrictions as the human role invoking them.
- **Ontology as Single Source of Truth**: Object Types, Link Types, and especially Action Types are governed centrally.
- **Data Markings & Security First**: Data Stewards/Information Security Officers define classification and access rules. All other roles must respect them.
- **Deterministic vs Generative Separation**: LLMs propose and reason; deterministic Functions/Actions execute with full auditability.
- **Generalizability**: Roles and interactions are abstract enough to apply to any domain with sensitive data and operational actions.

## Role Taxonomy

### 1. Ontology Administrator (Highest Schema Authority)
- **Power**: Absolute control over Object Types, Link Types, and **Action Types**.
- **Key Duty**: Defines what operations AI and users are allowed to perform.
- **Interaction**: Approves all new Action Types proposed by Function Developers or Agent Builders. Works with Data Stewards on security implications.
- **Security Note**: Can define Action Types that respect or enforce Data Markings.

### 2. Data Steward / Information Security Officer
- **Power**: Controls **Data Markings** (classification) and defines **Row-Level Security (RLS)** and **Object-Level Security** rules.
- **Key Duty**: Does **not** build applications. Governs who can see and act on what data.
- **Interaction**: Provides the security rules that Ontology Administrator, Action Invokers, and AIP Agents must follow. AIP Agents must never bypass these rules.

### 3. Function / Tool Developer (Palantir Functions style)
- **Power**: Writes deterministic code (TypeScript/Python/Rust) that becomes executable **Action Types**.
- **Key Duty**: Implements reliable, auditable, side-effect-aware logic that LLMs can safely call.
- **Interaction**: Proposes Action Types to Ontology Administrator. Must implement security context and Data Marking awareness inside functions.

### 4. Ontology Editor (Limited Scope)
- **Power**: Can modify specific, pre-approved Object Types or Link Types within a bounded scope.
- **Key Duty**: Day-to-day ontology maintenance without full admin rights.
- **Interaction**: Works under direction of Ontology Administrator. Cannot create new Action Types.

### 5. AIP Agent Builder / Prompt Engineer
- **Power**: Configures LLM agents, injects "Ontology of Thought", selects which **Action Types** the agent is allowed to use.
- **Key Duty**: Designs safe, effective agent behavior and tool-use policies.
- **Interaction**: Can only select Action Types that have been approved by Ontology Administrator. Must respect Data Markings defined by Data Stewards. Works closely with Function Developers on tool contracts.

### 6. Application Builder (Workshop / Slate Developer)
- **Power**: Builds low-code visual interfaces (dashboards, forms, workflows) powered by the ontology.
- **Key Duty**: Creates the human-facing applications where end users (Viewers and Action Invokers) work.
- **Interaction**: UI components must respect Data Markings and only expose approved Actions. Often works with Ontology Editors for data modeling in the UI.

### 7. Action Invoker / Operator (Most Operationally Critical)
- **Power**: Given explicit permission to invoke specific **Action Types** on objects they are authorized to see.
- **Example**: "Logistics_Manager" role can invoke `Ubah_Rute_Kargo` Action; "Logistics_Staff" cannot.
- **Key Duty**: The primary human users who execute real operational changes through the platform.
- **Interaction**: Their permissions are a combination of:
  - Data Markings / RLS (what they can see)
  - Action Type permissions (what they can do)
  - Object-Level rules

### 8. Viewer (Read-Only User)
- **Power**: Can only view objects, dashboards, and reports permitted by their Data Markings and role.
- **Key Duty**: Consumes information. Cannot modify data directly.
- **Interaction with AI**: If a Viewer asks an AIP Agent to change data or invoke an Action, the agent **must refuse** (enforced by security layer + agent prompt rules).

### 9. Forward Deployed Software Engineer (FDSE) / Forward Deployed Engineer
- **Power**: Embedded technical delivery role. Rapidly builds value inside customer environments using the above roles and ontology.
- **Key Duty**: Bridges product/platform capabilities with real operational problems. Provides feedback to improve ontology and Actions.
- **Interaction**: Works across all roles during deployment. Often acts as a temporary Ontology Editor or Application Builder on-site.

### 10. Deployment Strategist (DS)
- **Power**: Strategic planning and governance of deployments across multiple customers or domains.
- **Key Duty**: Defines deployment patterns, risk models, ontology maturity models, and scaling strategies.
- **Interaction**: Works with FDSEs and Ontology Architects to ensure repeatable, secure deployment playbooks.

### 11. Ontology Architect (Strategic)
- **Power**: Designs the overall ontology architecture, modularization, governance model, and alignment with business capabilities.
- **Interaction**: Guides Ontology Administrator on long-term schema strategy. Works with Data Stewards on security architecture.

### 12. Ontology Developer (Hands-on)
- **Power**: Implements ontology modeling, SHACL rules, data mappings, and validation under the direction of the Ontology Administrator and Architect.

## Role Interaction Matrix (Key Flows)

| Role                        | Can Define Action Types? | Can Invoke Actions? | Can See All Data? | Can Modify Ontology Schema? | Interacts Strongly With |
|-----------------------------|---------------------------|---------------------|-------------------|-----------------------------|-------------------------|
| Ontology Administrator     | Yes (Sole authority)     | Limited            | Via markings     | Full                       | Data Steward, Function Developer, Agent Builder |
| Data Steward / ISO         | No                       | No                 | No (defines rules)| No                         | Ontology Administrator, All roles (security enforcement) |
| Function/Tool Developer    | Proposes only            | For testing        | Test data only   | No                         | Ontology Administrator, AIP Agent Builder |
| AIP Agent Builder          | Selects only (approved)  | Via agent config   | No               | No                         | Ontology Administrator, Function Developer, Action Invoker |
| Action Invoker / Operator  | No                       | Yes (assigned)     | Only permitted   | No                         | Application Builder, AIP Agents, Data Steward rules |
| Viewer                     | No                       | No                 | Only permitted   | No                         | AIP Agents (read-only mode) |
| Application Builder        | No                       | Via UI             | Only permitted   | Limited (via Editor)       | Action Invoker, Ontology Editor |
| Forward Deployed SE        | Proposes / temporary     | During deployment  | Context-specific | Temporary (scoped)         | All roles during engagement |

## OAG (Ontology-Augmented Generation) Safety Rules

- Every AIP Agent must operate under a specific **user role context** (Viewer, Action Invoker, etc.).
- Agents can only propose or invoke **pre-approved Action Types**.
- All data retrieval and Action execution must respect **Data Markings + RLS + Object-Level Security**.
- Deterministic Functions (written by Function Developers) provide the safe execution layer. LLMs reason and decide *when* to call them.
- Provenance and audit logging are mandatory for every Action invocation (human or AI).

## Domain Adaptation Notes (Defense / Logistics / Health)

- **Defense**: Stronger emphasis on classification levels (Secret, Top Secret), compartmented access, and strict Action Type auditing. Ontology Administrator role becomes extremely high-stakes.
- **Logistics**: Heavy use of Action Invoker roles (route changes, inventory movements). Data Markings may focus on commercial sensitivity + regulatory compliance.
- **Healthcare**: Patient data requires strict Row-Level Security (patient-level access). Action Types often involve clinical decision support with heavy validation. Data Stewards work closely with medical governance bodies.
- **General Pattern**: The taxonomy remains the same; only the specific Action Types, classification schemes, and regulatory overlays change.

This taxonomy creates clear accountability, prevents privilege escalation, and enables safe, auditable AI augmentation of operational workflows across any domain.