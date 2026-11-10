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

This initial repository baseline contains documentation and safeguards.

Code, technical evidence, tender documents, and historical outputs
require separate review before migration.

## Governance

The Project owner approves requirements, scope, technical dispositions,
and milestones. Owner approval does not replace missing engineering
confirmation.

Repository changes do not authorize new OKKI retrieval, bulk extraction,
model/API integration, or feature development.

## Documentation

- DATA_POLICY.md — confidentiality and evidence-handling rules.
- BACKLOG.md — proposed repository tasks and acceptance criteria.

Detailed requirements, design decisions, and current status remain in
the existing Project documents until reviewed migration is completed.