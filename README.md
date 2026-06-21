# Skunkwork Skills

Agent skills for Claude Code / Windsurf / Devin — Skunk Works methodology applied to organizational design, ontology engineering, ISO compliance, AI agent development, and mission-critical operations.

## Overview

34 skills in Anthropic SKILL.md format. Each skill directory contains a `SKILL.md` with YAML frontmatter (`name`, `description`) and markdown instructions, plus optional `references/`, `assets/`, and `scripts/` subdirectories.

Compatible with [skills.sh](https://skills.sh) registry — see [`skills.sh.json`](skills.sh.json).

Inspired by Lockheed Martin Skunk Works principles: small teams, radical autonomy, cross-functional delivery, minimal bureaucracy.

## Skill Catalog

### AI & Agent Development
| Skill | Description |
|-------|-------------|
| `aip-agent-builder-prompt-engineer` | Build AIP agents: prompt engineering, tool selection, agent lifecycle |
| `aip-engineer` | AIP platform engineering — agent integration, deployment, monitoring |
| `meta-skill` | Skill authoring framework — create, test, maintain skills |
| `function-tool-developer` | Action Type implementation: deterministic tools for agent invocations |
| `skunkworks-agent-coder` | Skunk Works methodology for agent development sprints |
| `skunkworks-organizational-model` | Kelly Johnson's 14 Rules — team structure, autonomy, rapid innovation |
| `action-invoker-operator` | Action execution, lifecycle management, error handling |
| `autonomous-operations-optimization` | Autonomous systems ops — decision loops, monitoring, failover |

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

### Operations & Automation
| Skill | Description |
|-------|-------------|
| `employee-management` | People ops — performance, hiring, retention, compliance |
| `rpa-bridges-for-legacy-systems` | RPA integration — connect legacy systems without full migration |
| `viewer-read-only-user` | Read-only access governance — audit, monitoring, data protection |

## Skills Registry

[`skills.sh.json`](skills.sh.json) — compatible with https://skills.sh for discovery and indexing.

## Repository Structure

```
skunkwork-skills/
├── README.md                       # this file
├── skills.sh.json                  # skills.sh registry
├── .windsurfrules                  # Windsurf global rules (skill index)
├── .devin/
│   └── rules.md                    # Devin rules (skill index)
├── <skill-name>/                   # 34 skill directories
│   ├── SKILL.md                    # YAML frontmatter + markdown instructions
│   ├── references/                 # optional reference docs
│   ├── assets/                     # optional assets
│   └── scripts/                    # optional executable scripts
└── Documents/
    └── AI_LEAD_ABC/
        └── SKILL-AGENT/
            ├── README.md           # original project README
            └── skills.sh.json      # original registry copy
```

## Installation

### Claude Code

```bash
# Clone the repo
git clone https://github.com/daemon-blockint-tech/Skunkwork-skills.git

# Copy skills to Claude Code skills directory
cd Skunkwork-skills
for d in */; do
  if [ -f "$d/SKILL.md" ]; then
    cp -r "$d" ~/.claude/skills/
  fi
done
```

### Windsurf

The `.windsurfrules` file at the repo root contains the skill index. Copy it to your home directory:

```bash
cp .windsurfrules ~/.windsurfrules
```

### Devin

Copy rules and create workflow files:

```bash
mkdir -p ~/.devin/workflows
cp .devin/rules.md ~/.devin/rules.md

for d in */; do
  name=$(basename "$d")
  if [ -f "$d/SKILL.md" ]; then
    cat > ~/.devin/workflows/${name}.md << EOF
---
description: $(awk '/^description:/{sub(/^description: /,""); print; exit}' "$d/SKILL.md")
---
# Skill: ${name}
Load and follow ~/.claude/skills/${name}/SKILL.md
EOF
  fi
done
```

## Usage

Skills are triggered by task context. Load the relevant `SKILL.md` when a task matches the skill's description. Skills compose naturally — use multiple when a task spans domains.

### Claude Code

Skills in `~/.claude/skills/` are auto-discovered. Reference by name in conversation.

### Windsurf / Devin

Use as slash commands (e.g., `/skunkworks-agent-coder`) or reference the workflow file directly.

## License

Private — daemon-blockint-technologies.
