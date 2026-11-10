# Repository Backlog

Status: Proposed repository setup tasks, not authorization to execute.
This is not a replacement for the Project's authoritative status record.

## R1 — Establish the documentation baseline

Status: In progress
Owner / approver: Erick Merino
Scope: Repository documentation and confidentiality safeguards only.

### Objective

Establish a clear repository baseline describing the project's purpose,
current phase, assessment boundaries, confidentiality rules, and proposed
next tasks—without authorizing implementation or data migration.

### Acceptance checklist

- [x] README.md states the project's purpose and intended outcome.
- [x] README.md identifies the current phase as design and feasibility
      validation, not an operational matching service.
- [x] README.md separates intended behavior from validated behavior
      and preserves human-review and engineering-confirmation boundaries.
- [x] DATA_POLICY.md defines prohibited content and reviewed,
      minimized evidence-handling requirements.
- [x] BACKLOG.md includes proposed tasks, acceptance criteria,
      and explicitly deferred activities.
- [x] Rename .gitignore.txt to .gitignore, preserving its contents.
- [x] Confirm that .gitignore exists at the repository root and
      .gitignore.txt no longer exists.
- [x] The inspected baseline contains only the four preparation files;
      no code, product datasets, or tender attachments are included.
- [ ] Review the final changes for credentials, signed access links,
      and other prohibited sensitive content.
- [ ] Record the owner's explicit acceptance of this baseline.

### Review evidence

Repository inspection: 2026-11-10
Inspected branch: main
Inspected commit: 119d9d9213ecdab2b9650084ff6d3e17b2c1d4e9

Files inspected:
- README.md
- DATA_POLICY.md
- BACKLOG.md
- .gitignore.txt

Finding:
The documentation baseline is present. The ignore file requires renaming
to .gitignore. Owner acceptance is not recorded in this task.

Review limitation:
This was a current-file and branch/pull-request inspection, not a
full-history secret audit or software validation.

Correction commit / pull request: Pending
Final review date: Pending

### Completion rule

Mark R1 Complete only after:
1. The ignore filename is corrected and verified.
2. The final baseline receives a confidentiality review.
3. The owner explicitly accepts the baseline.

### Owner acceptance

Decision: Pending
Decision date: Pending
Approved commit: Pending
Notes: Pending

### Boundaries

Completing R1 does not authorize:
- Migration of Project documents, code, or product evidence.
- New OKKI retrieval or bulk extraction.
- Script execution, API integration, or feature development.

R1 completion does not establish pilot acceptance, technical compliance,
engineering approval, or production readiness.

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
