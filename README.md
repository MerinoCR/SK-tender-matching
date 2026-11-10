# Saikang Tender Matching

## Purpose

Develop an evidence-based, human-assisted workflow that interprets government-tender specifications, selects the appropriate OKKI product subfamily, and assesses exact Saikang SKUs against the requirements.

The intended outcome is zero, one, or up to two independently supported compliant candidates. Conditional configurations and near matches remain separate from compliant results.

## Current phase

Design and feasibility validation. This repository is not an operational matching service. Repository setup and policy unit tests do not establish full pilot acceptance, autonomous matching accuracy, engineering approval or production readiness.

## Intended workflow

Tender interpretation → subfamily selection → authorized scoped retrieval → exact-SKU evidence assessment → owner-policy disposition → human review.

## Assessment principles

- Treat the tender's functional configuration as a boundary; extra functions are not automatically acceptable.
- Assess exact SKUs independently; never transfer features between related SKUs or models.
- Use relevant original English and Chinese descriptions.
- Preserve missing evidence and contradictions.
- Apply the dated owner rules with explicit provenance rather than presenting assumptions as quoted facts.
- Distinguish documentary assessment, owner-policy acceptance, customization requests, engineering confirmation and final-offer approval.
- Do not force two compliant results when fewer qualify.
- Keep proposed behavior separate from tested behavior.

## Current owner rules

[Standing owner rules — 2026-11-10](OWNER_RULES_2026_11_10.md) supersedes contrary defaults in the three core documents only for its twelve recorded topics. It covers load basis, positioning, bumpers, storage, antistatic wheels, IV arrangements, backrest customization, rigid four-section construction, full-length cassette travel, rail details, fifth-wheel diameter and separate customizable mattresses. Original tender wording and historical records are preserved.

## Repository scope and code status

The repository contains the documentation baseline, reviewed migration copies of the three core Project documents, their provenance/redaction log, and a minimal new policy module with synthetic tests. Existing Project pilot code, product datasets, tender attachments and supporting historical reports have not been migrated by this change.

- `policy/owner_rules.py`: versioned policy dispositions from reviewed structured exact-SKU facts.
- `policy/test_owner_rules.py`: synthetic unit tests, not product evidence.
- Run: `python -m unittest discover -s policy -p 'test_*.py' -v`

Twelve test methods passed in the response Python environment before the proposed commit. Existing prototype integration and regressions remain pending. The module does not parse tenders, extract facts, retrieve products or generate a final shortlist.

## Governance

The Project owner approves requirements, scope, technical dispositions, commercial release and milestones. Owner approval does not replace missing engineering confirmation. This change does not authorize new OKKI retrieval, bulk extraction, model/API integration or unrelated feature development.

## Documentation

- [Project brief and requirements](01_PROJECT_BRIEF_AND_REQUIREMENTS.md) — purpose, requirements and approved pilot criteria.
- [Design and technical reference](02_DESIGN_AND_TECHNICAL_REFERENCE.md) — observations and design boundaries.
- [Status and next steps](03_STATUS_AND_NEXT_STEPS.md) — detailed historical status and decision record, read with the dated owner-rule addendum.
- [Standing owner rules and integration backlog](OWNER_RULES_2026_11_10.md) — current superseding decisions, tested scope and remaining acceptance criteria.
- [Data policy](DATA_POLICY.md) — confidentiality and evidence handling.
- [Repository backlog](BACKLOG.md) — baseline repository tasks; policy-specific tasks are in the dated addendum.
- [Migration redaction log](REDACTION_LOG.md) — migration review limitations; no sensitive values reproduced.

### Authority and evidence availability

The three core documents remain migration copies with their original provenance sections and dated historical entries. Later explicit decisions supersede earlier statements only within recorded scope. Supporting material is not claimed to have been independently validated merely because a document references it.

No credentials, signed access links, raw product exports, commercial data or tender attachments are included in this policy update.
