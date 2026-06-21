---
name: vanguard-audit
description: Use for Vanguard security vulnerability audits and constraint compliance checks in Orion autonomous deployment systems or similar Kubernetes setups. Triggers on requests to audit clusters for CVEs, evaluate security policies, review SecurityVulnerability evaluator, check CVSS thresholds, perform deployment readiness audits, or analyze active vulnerabilities in connected or air-gapped environments.
---

# Vanguard Audit

## Overview

This skill specializes in security-focused audits for constraint-based deployment engines like Orion. It leverages knowledge of the SecurityVulnerability evaluator, VulnerabilityStore, CVE handling, CVSS threshold policies, and integration with NodeHealth and MaintenanceWindow constraints to ensure safe deployments.

## Instructions

When the user requests a Vanguard audit or security vulnerability analysis:

1. Identify the scope: cluster name, product IDs, active CVEs if provided, or specific policy thresholds.
2. Use GitHub connected tools (search_connected_tools, call_connected_tool with github___ prefix) to inspect the latest Orion codebase when code review or evaluator logic clarification is needed — e.g., fetch evaluator_security_vulnerability.go, engine.go, or relevant ADRs from docs/adr/.
3. Recall and apply Orion's constraint evaluation flow: the Hub evaluates MaintenanceWindow, NodeHealth, and SecurityVulnerability concurrently per polling cycle from the Agent. SECURITY_VULNERABILITY returns PROCEED only if no active CVEs exceed the policy's BlockedCVSSThreshold.
4. For CVE analysis:
   - List provided active_cves from ClusterHealth.
   - Resolve CVSS scores via VulnerabilityStore (or note noop behavior in tests).
   - Flag any CVE with score >= threshold as blocking (leads to ROLLBACK or HOLD decision).
   - Fail-safe: treat lookup errors as blocking.
5. Cross-reference with other evaluators: a HOLD from maintenance window or unhealthy nodes takes precedence or combines with vulnerability results in the engine aggregator.
6. Provide actionable recommendations: update images to patched versions, adjust policy thresholds, or investigate specific CVEs using external knowledge if needed.
7. When reviewing code or suggesting changes to Orion:
   - Reference exact file paths from the repository tree (e.g., internal/hub/engine/evaluator_security_vulnerability.go, internal/hub/engine/engine.go).
   - Suggest improvements aligned with existing ADRs (e.g., run-to-completion evaluation, storage layer).
   - Use create_pull_request or other GitHub tools only after user confirms.
8. Output structured audit report: summary of passed/failed constraints, specific blocking reasons, recommended next actions, and adaptive hint implications (e.g., shorter NextEvalHintSec on ROLLBACK).

Always run-to-completion: evaluate all relevant constraints even if one fails early. Prioritize fail-safe posture for security.

Do not fabricate CVSS scores or CVE data; base analysis only on provided inputs or fetched code/docs.