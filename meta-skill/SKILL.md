---
name: meta-skill
description: Meta-skill for creating, versioning, validating, curating, and orchestrating other skills. Includes cross-skill consistency checks, dependency mapping, role interaction modeling, and best practices for building coherent skill ecosystems — trigger when designing new skills, maintaining skill libraries, ensuring consistency across multiple skills, or building meta-level orchestration for agent capabilities
---

# Meta-Skill: Skill Creation, Orchestration & Governance

This is a **meta-skill** — a skill whose primary purpose is to help create, improve, validate, version, and orchestrate other skills. It encodes the methodology for building high-quality, consistent, and interoperable skill libraries.

## Core Purpose

- Provide a repeatable, high-quality process for creating new skills (beyond the basic init script).
- Enable cross-skill consistency, dependency management, and conflict detection.
- Support versioning, deprecation, and evolution of the skill ecosystem.
- Facilitate the creation of role taxonomies, interaction matrices, and governance frameworks (especially useful for complex domains like AIP, defense, logistics, or healthcare).

## When to Activate This Skill

- Designing or refactoring multiple interrelated skills.
- Building a new domain-specific skill library (e.g., AIP roles, UAV engineering, ontology governance).
- Performing consistency audits across existing skills.
- Creating role interaction matrices or governance models.
- Versioning or deprecating skills in a controlled way.

## Meta-Skill Workflow (Use This Process)

### 1. Skill Identification & Scoping
- Clearly define the skill's name (kebab-case), primary trigger scenarios, and what the base model does **not** already know.
- Identify whether it is a **role skill** (persona/responsibility), **methodology skill** (process/workflow), **technical skill** (tooling/code), or **meta skill**.
- Map dependencies on other skills (e.g., ontology-developer depends on ontology-architect).

### 2. Frontmatter Design (Critical)
- Write a precise `description` that serves as the trigger condition.
- Follow strict rules: plain YAML scalar, no `: `, no angle brackets, concise but descriptive.
- Include both "what" and "when to use".

### 3. Content Structure (SKILL.md)
- Start with clear mandate and core principles.
- Use imperative language.
- Include sections for: Responsibilities, Workflow/Process, Anti-Patterns, Cross-Role/Skill Interactions, Integration with OAG or other capabilities.
- Keep under 500 lines; move detailed examples, matrices, or long templates to `references/` or `assets/`.

### 4. Supporting Resources
- **assets/**: Reusable templates (checklists, matrices, kickoff templates, permission matrices).
- **references/**: Patterns, examples, governance frameworks, domain-specific adaptations (defense, logistics, health).
- **scripts/**: Validation scripts, consistency checkers, dependency mappers (Python helpers).

### 5. Cross-Skill Consistency Checks (Meta Level)
When creating or updating skills, run these checks:
- **Terminology consistency**: Do roles use the same terms for "Action Type", "Object Type", "Data Markings", "OAG", etc.?
- **Dependency mapping**: Does this skill correctly reference related skills (e.g., aip-agent-builder-prompt-engineer should reference ontology-administrator and function-tool-developer)?
- **Security & Governance alignment**: Do all skills that touch data/actions respect Data Steward and Ontology Administrator authority?
- **Role interaction clarity**: Is it clear how this role interacts with others (especially Viewer vs Action Invoker vs Ontology Administrator)?
- **Generalizability**: Is the skill usable beyond one domain (defense, logistics, healthcare, manufacturing)?

### 6. Versioning & Governance
- Use semantic versioning for skills when significant changes occur.
- Maintain a changelog in `references/CHANGELOG.md` for major skills.
- When deprecating a skill, provide migration guidance to successor skills.

### 7. Validation
- Run structural validation (`validate-skill.sh`).
- Perform content review against this meta-skill's principles.
- Test trigger conditions by simulating user queries.

## Recommended Supporting Assets (Create These When Building Skill Libraries)

- Role Permission & Interaction Matrix (see AIP Role Taxonomy document)
- Action Type Governance Checklist
- Data Markings & Security Policy Template
- Cross-Skill Dependency Graph (text or Mermaid)
- Skill Creation Checklist (derived from this meta-skill)

## Anti-Patterns at the Meta Level

- Creating isolated skills that duplicate knowledge or contradict each other.
- Writing skills that are too generic (base model already knows) or too narrow (only useful in one very specific context).
- Ignoring role interactions and security boundaries when defining AIP-style skills.
- Failing to make skills generalizable across domains (defense, logistics, health, etc.).

## Usage in Complex Environments (Defense, Logistics, Health)

This meta-skill is particularly valuable when building skill libraries for regulated or high-stakes domains:
- Ensure all skills explicitly address Data Markings, classification, and least-privilege principles.
- Make roles (Viewer, Action Invoker, Ontology Administrator) clearly separated with defined handoffs.
- Include domain adaptation notes in references/ (e.g., how Action Types differ in defense vs commercial logistics).

Mastering this meta-skill allows you to build coherent, trustworthy, and maintainable skill ecosystems rather than collections of disconnected instructions. It turns skill creation from an ad-hoc activity into a governed engineering discipline.