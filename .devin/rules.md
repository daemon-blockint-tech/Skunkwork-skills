# Devin Rules for SKILL-AGENT

This project holds 34 custom AI skills in Anthropic SKILL.md format. Skills are in subdirectories with SKILL.md + optional references/, assets/, scripts/.

## Working with Skills

- Each skill dir has SKILL.md with YAML frontmatter (name, description) + markdown instructions
- Optional REFERENCE.md in refs/ for supplemental context
- Optional scripts/ for executable code
- Skills compose — use multiple when relevant

## Installed Locations

Skills are also installed to:
- ~/.claude/skills/<name>/ — Claude Code uses natively
- ~/.windsurfrules — Windsurf global rules (index only, load SKILL.md for full content)

## Skill Index

### Agent & Builder
- action-invoker-operator — deterministic tool execution
- aip-agent-builder-prompt-engineer — AIP agent config
- aip-engineer — AIP engineering
- application-builder-workshop-slate — workshop apps
- function-tool-developer — TypeScript/Python/Rust function types
- meta-skill — skill creation/validation/orchestration
- skunkworks-agent-coder — rapid agent development
- skunkworks-organizational-model — Skunk Works principles

### Ontology
- ontology-administrator — schema governance
- ontology-architect — enterprise ontology strategy
- ontology-augmented-generation — OAG/OG-RAG
- ontology-developer — OWL/RDF/SHACL/SPARQL
- ontology-editor — ontology editing

### Data/Security
- data-steward-information-security-officer — Data Markings, RLS, OLS
- vanguard-audit — K8s CVE audits

### Business/Finance
- autonomous-operations-optimization — enterprise AI ops
- business-foundation — strategy, product, scaling
- business-planning — roadmaps, KPIs
- business-revenue-forecasting — revenue models
- cash-flow-management — cash flow
- financial-report-analysis — P&L, balance sheets
- working-capital-management — crisis strategies

### People/HR
- employee-management — performance
- human-capital-and-smart-interviewing — hiring

### ISO Standards
- iso-9001-quality-management
- iso-14001-environmental-management
- iso-27001-information-security
- iso-iec-20000-it-service-management
- iso-iec-42001-artificial-intelligence

### Forward Deployed
- forward-deployed-engineer — customer-embedded delivery
- forward-deployed-software-engineer — field engineering
- rpa-bridges-for-legacy-systems — RPA for legacy integration

### Other
- uav-uas-aerodynamic-designer
- viewer-read-only-user
