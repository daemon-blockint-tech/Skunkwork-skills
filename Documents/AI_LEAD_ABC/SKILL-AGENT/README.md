# Skunkwork Skills

Agent skills for Hermes / Claude Code — Skunk Works methodology applied to organizational design, ontology engineering, ISO compliance, AI agent development, and mission-critical operations.

## Overview

34 skills packed as `.zip` files. Each contains a `SKILL.md` with YAML frontmatter compatible with [skills.sh](https://skills.sh) and Claude Code skills ecosystem.

Inspired by Lockheed Martin Skunk Works principles: small teams, radical autonomy, cross-functional delivery, minimal bureaucracy.

## Skill Catalog

### AI & Agent Development
| Skill | Description |
|-------|-------------|
| `aip-agent-builder-prompt-engineer` | Build AIP agents: prompt engineering, tool selection, agent lifecycle |
| `aip-engineer` | AIP platform engineering — agent integration, deployment, monitoring |
| `meta-skill` | Skill authoring framework — create, test, maintain Hermes/Claude skills |
| `function-tool-developer` | Action Type implementation: deterministic tools for agent invocations |

### Ontology Engineering
| Skill | Description |
|-------|-------------|
| `ontology-architect` | Enterprise ontology architecture — domains, types, relationships |
| `ontology-developer` | Implementation: schema, object types, action types, validation |
| `ontology-editor` | Ontology maintenance — versioning, deprecation, impact analysis |
| `ontology-administrator` | Governance — approvals, naming, change control, lifecycle |
| `ontology-augmented-generation` | OAG patterns — ontology-grounded RAG for agents |

### ISO / Compliance
| Skill | Description |
|-------|-------------|
| `iso-9001-quality-management` | QMS — processes, audits, continuous improvement |
| `iso-27001-information-security` | ISMS — risk assessment, controls, certification |
| `iso-14001-environmental-management` | EMS — environmental policy, compliance, sustainability |
| `iso-iec-20000-it-service-management` | ITSM — service delivery, SLAs, incident management |
| `iso-iec-42001-artificial-intelligence` | AI management — risk, governance, ethical compliance |
| `data-steward-information-security-officer` | Data classification, marking, access governance |
| `vanguard-audit` | Security audit & compliance verification |

### Business & Finance
| Skill | Description |
|-------|-------------|
| `business-foundation` | Entity formation, structure, governance fundamentals |
| `business-planning` | Strategic planning, OKRs, roadmaps |
| `business-revenue-forecasting` | Revenue modeling, pipeline analysis, projections |
| `cash-flow-management` | Working capital, liquidity, CCC optimization |
| `financial-report-analysis` | Financial statement analysis, ratio analysis |
| `working-capital-management` | Working capital strategies, inventory/AR/AP optimization |
| `human-capital-and-smart-interviewing` | Talent strategy, structured interviewing, competency assessment |

### Forward Deployed & Engineering
| Skill | Description |
|-------|-------------|
| `forward-deployed-engineer` | Customer-facing engineering — requirements, delivery, escalation |
| `forward-deployed-software-engineer` | Production deployment, integration, customization |
| `application-builder-workshop-slate` | Rapid prototyping — workshop facilitation, MVP builds |
| `uav-uas-aerodynamic-designer` | UAV/UAS design — aerodynamics, structures, systems integration |

### Skunk Works Core
| Skill | Description |
|-------|-------------|
| `skunkworks-organizational-model` | Kelly Johnson's 14 Rules — team structure, autonomy, rapid innovation |
| `skunkworks-agent-coder` | Skunk Works methodology for agent development sprints |

### Operations & Automation
| Skill | Description |
|-------|-------------|
| `action-invoker-operator` | Action execution, lifecycle management, error handling |
| `autonomous-operations-optimization` | Autonomous systems ops — decision loops, monitoring, failover |
| `employee-management` | People ops — performance, hiring, retention, compliance |
| `rpa-bridges-for-legacy-systems` | RPA integration — connect legacy systems without full migration |
| `viewer-read-only-user` | Read-only access governance — audit, monitoring, data protection |

## Skills Registry

[`skills.sh.json`](skills.sh.json) — compatible with https://skills.sh for discovery and indexing.

```json
{
  "name": "Skunkwork Skills",
  "description": "Skunk Works methodology skills — organizational design to ontology engineering",
  "skills": ["action-invoker-operator", "...", "working-capital-management"]
}
```

## Repository Structure

```
skunkwork-skills/
├── skills.sh.json              # skills.sh registry
├── README.md                   # this file
├── *.zip                       # skill packages (SKILL.md each)
├── action-type-governance-checklist.md
├── SKILL.md                    # working-capital-management skill (root)
├── assets/                     # deployment & governance checklists
│   ├── action-type-governance-checklist.md
│   ├── deployment-checklist.md
│   ├── ontology-architecture-checklist.md
│   ├── ontology-development-checklist.md
│   ├── prompt-templates.md
│   ├── skunkworks-project-kickoff.md
│   └── skunkworks-roles-summary.md
├── references/                 # reference docs & patterns
│   ├── aip-role-taxonomy-interaction-matrix.md
│   ├── fde-playbook-patterns.md
│   ├── kelly-johnson-14-rules.md
│   ├── key-concepts-and-papers.md
│   ├── ontology-architecture-patterns.md
│   ├── practical-ontology-development-tips.md
│   ├── sample-ecommerce-ontology.json
│   ├── simple-ecommerce-ontology.md
│   └── skunkworks-principles-adapted.md
└── scripts/
    └── ontology_to_prompt_text.py
```

## Usage

### Hermes

Skills auto-discovered via skills directory. Load with:

```
hermes skill load <name>
```

### Claude Code

Load a skill by referencing its `SKILL.md`:

```
Claude Code: load skill from path/to/skunkworks-organizational-model/SKILL.md
```

### Manual

Unzip any `.zip` and point your agent to the `SKILL.md` inside.

## License

Private — daemon-blockint-technologies.
