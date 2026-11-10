# Saikang Tender Matching

## Purpose

Develop an evidence-based, human-assisted workflow that interprets
government-tender specifications, selects the appropriate OKKI product
subfamily, and assesses exact Saikang SKUs against the requirements.

The intended outcome is zero, one, or up to two independently supported
compliant candidates. Conditional configurations and near matches must
remain separate from compliant results.

## Current phase

Design and feasibility validation.

Existing Project work includes bounded pilot components and documentary
assessments. Their migration into this GitHub repository is a separate
reviewed activity.

This repository is not an operational matching service.
Repository setup does not establish full pilot acceptance, autonomous
matching accuracy, engineering approval, or production readiness.

## Intended workflow

Tender interpretation → subfamily selection → authorized scoped
retrieval → exact-SKU evidence assessment → human review.

## Assessment principles

- Treat the tender's functional configuration as a boundary.
- Do not assume extra functions are acceptable.
- Assess each exact SKU independently; never transfer features
  between related SKUs or models.
- Use relevant original English and Chinese descriptions.
- Preserve missing evidence, ambiguity, and contradictions.
- Distinguish documentary assessment from engineering confirmation.
- Do not force two compliant results when fewer qualify.
- Keep proposed behavior separate from tested behavior.

## Repository scope

This branch contains the documentation baseline and reviewed migration
copies of the three core Project documents, with source provenance and
an accompanying redaction log.

Code, product datasets, tender attachments, and supporting historical
reports are not included in this migration. They require separate review
and authorization before migration.

## Governance

The Project owner approves requirements, scope, technical dispositions,
and milestones. Owner approval does not replace missing engineering
confirmation.

Repository changes do not authorize new OKKI retrieval, bulk extraction,
model/API integration, or feature development.

## Documentation

- [Project brief and requirements](01_PROJECT_BRIEF_AND_REQUIREMENTS.md)
  — purpose, assessment rules, requirements, and approved pilot criteria.
- [Design and technical reference](02_DESIGN_AND_TECHNICAL_REFERENCE.md)
  — design boundaries, technical observations, and design changes.
- [Status and next steps](03_STATUS_AND_NEXT_STEPS.md)
  — authoritative detailed current-status and decision record.
- [Data policy](DATA_POLICY.md)
  — confidentiality and evidence-handling rules.
- [Repository backlog](BACKLOG.md)
  — repository tasks and acceptance criteria.
- [Migration redaction log](REDACTION_LOG.md)
  — redaction type, location, and review limitations; no sensitive
  value is reproduced.

### Documentation authority and evidence availability

The three core documents are migration copies from the existing Project.
Their provenance sections identify the source snapshot and migration
changes.

Dated historical entries are retained. Later explicit decisions supersede
earlier statements only within their recorded scope. Migration does not
approve every draft statement.

Supporting reports, source datasets, code, and tender attachments
referenced by these documents are not included unless separately migrated.
References to that evidence are not claims that it has been independently
inspected or validated in this repository.

Document 03 remains the authoritative detailed status and decision record.
BACKLOG.md tracks repository tasks rather than a competing pilot status.

Repository migration does not establish full pilot acceptance,
engineering approval, or production readiness.
