# Repository Backlog

Status: Proposed repository setup tasks, not authorization to execute.
This is not a replacement for the Project's authoritative status record.

## R1 — Establish the documentation baseline

Acceptance criteria:
- README states the purpose and current phase.
- Operational and validation limitations are explicit.
- Confidentiality rules and ignore rules are included.
- No code, product dataset, tender attachment, or credential is included.
- Owner reviews the initial changes.

## R2 — Migrate authoritative project documentation

Acceptance criteria:
- Review the current brief, technical reference, and status documents.
- Remove prohibited sensitive content without erasing material decisions.
- Preserve decision dates, evidence limitations, and historical context.
- Identify the authoritative status record and avoid competing summaries.
- Record the source version and migration date.
- Review the migration diff before approval.

## R3 — Inventory existing pilot code before migration

Acceptance criteria:
- Identify each script's purpose, dependencies, inputs, and outputs.
- Separate recorded test results from tests actually rerun.
- Check for embedded credentials, signed links, and sensitive fixtures.
- Distinguish reusable modules from historical standalone versions.
- Do not execute scripts or make network requests merely to inventory them.
- Propose a minimal migration set for separate approval.

## R4 — Record the remaining pilot acceptance gap

Acceptance criteria:
- Carry forward the existing compliance-gate demonstration gap accurately.
- Keep the single-eligible-result example and substantive extra-function
  handling visible.
- Do not reopen closed owner decisions or imply a new test has run.
- Any controlled examples require separate scope authorization.
- Full original pilot acceptance requires an explicit owner decision.

## Deferred

- New OKKI extraction or additional category capture.
- Bulk catalog migration.
- Autonomous matching or automatic shortlisting.
- New API integrations or user interfaces.
- Production deployment.

Deferred items are not authorized by repository creation or documentation
migration.