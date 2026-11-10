# Project Brief and Requirements

Status: Draft for review  
Last updated: 2026-11-09
Current phase: Design and feasibility validation

## Repository migration provenance

- Source: Saikang Tender Matching — Design & Development Project.
- Source filename: 01_PROJECT_BRIEF_AND_REQUIREMENTS.md.
- Source snapshot date: 2026-11-10
- Repository migration date: 2026-11-10
- Migration changes: Provenance section added; complete local copy reviewed for prohibited sensitive content; no redactions identified as necessary.
- Source preservation: The original Project file was not modified.

This is a repository copy of the source document. Migration does not
approve its draft content, change historical decisions, or establish
new implementation or validation results.

Supporting files referenced in this document may remain in the Project
and are not necessarily included in this repository.

## Purpose and evidence basis

The unfinished Saikang Tender Matching program is intended to help assess government-tender specifications against exact Saikang SKUs and identify up to two compliant candidates, supported by evidence. It is not an established matching service, and these drafts do not approve an architecture or authorize implementation.

- **Verified:** The existing Project file repository was empty when reviewed for these drafts. No Project knowledge pages were available after synchronization.
- **Verified:** The available historical evidence comprises `OKKI_Tender_Matching_Handoff.md`, the conversation of 2026-11-02 to 2026-11-03, and the user's handoff-adoption message of 2026-11-03.
- **Evidence limitation:** Historical sample analyses and script checks are attributed to those records, not independently reproduced. See `03_STATUS_AND_NEXT_STEPS.md` for availability and test status.
- **Labels:** “Verified” identifies directly inspected evidence or explicitly qualified historical observations; “Agreed requirement” identifies user instructions or decisions; “Proposed” identifies suggestions awaiting approval or testing; “Open question” identifies unresolved matters.

## Problem and intended users

Tender items must be matched to the correct functional configuration, not merely to similar product names. The historical discussion reports incomplete technical fields, multilingual descriptions, SKU-specific configurations and classification gaps; these make unsupported recommendations a material risk.

- **Agreed requirement, primary user:** Saikang sales staff preparing technical responses to government-tender inquiries.
- **Agreed requirement, approval ownership (user decision, 2026-11-03):** The Project owner (the user) is the sole approver for requirements, taxonomy/scope, technical findings, commercial release and milestone decisions. Specialist evidence may be requested when necessary; the owner's approval does not substitute for missing engineering confirmation.
- **Agreed requirement, outcome:** An evidence-based shortlist of zero, one or two exact SKUs, with requirement-level findings, gaps and contradictions. Document-based compliance must remain separate from engineering confirmation and final tender eligibility.

## Proposed workflow

**Approved scope rule, 2026-11-09:** Always omit installation and consumables from program evaluation, technical comparison outputs, clarification requests and compliance blockers. They are excluded from the evaluated scope, not automatically compliant or pending. Preserve original tender wording and historical records without altering them; this internal scope decision does not amend the tender or demonstrate that a product requires neither. Required mattresses and technical accessories remain in scope.

**Approved load-assessment rule, 2026-11-09:** When SKU load data do not permit a clear requirement comparison, label the finding “Pendiente de revisión humana” and retain the reason and original ratings. Do not infer a pass or failure, choose the most favorable rating or invent a load basis. Distinguish unclear/missing/conflicting SKU data from ambiguous tender wording; either may require human review, but the cause must remain explicit. Clear evidence can still support a documentary finding when the applicable tender basis is also clear. This is a documented assessment rule, not a claim of implemented software behavior.

`OKKI taxonomy → tender interpretation → subfamily selection → scoped technical-data retrieval → Perplexity comparison → engineering/commercial review`

The user chose taxonomy-first, subfamily-scoped matching and simple technical-text retrieval rather than a bulk catalog project. The following component-level workflow is proposed for validation, not described as implemented.

- **Taxonomy preparation:** Establish authorized family/subfamily IDs, original names, parent relationships and functional meanings. Verify completeness and parent-filter descendant behavior before using the map.
- **Tender interpretation:** Extract equipment type, mandatory functions, configuration limits, exclusions, preferred features, units, tolerances and documentary requirements. Retain the original wording and requirement references.
- **Subfamily selection:** Justify the selected IDs against the tender. Obtain user review in the pilot; flag ambiguity rather than silently expanding to another functional class.
- **Scoped retrieval:** Retrieve all authorized records in the approved scope, retaining original identifiers and English/Chinese technical fields. Provide a compact file and a scope/completeness record.
- **Perplexity comparison:** Assess every supplied in-scope SKU against every requirement, using explicit batches if necessary. Produce an evidence matrix and up to two compliant candidates within the assessed scope.
- **Human review:** Resolve conflicts and missing evidence, confirm the exact offerable configuration, and record the engineering/commercial decision. An AI finding is not certification.

See `02_DESIGN_AND_TECHNICAL_REFERENCE.md` for component boundaries and the proposed handoff.

## Functional requirements and boundaries

- **Agreed requirement, exact identity:** Preserve SKU ID/code, model and configuration. Do not deduplicate configurations by model name or transfer features between related SKUs.
- **Agreed requirement, multilingual evidence:** Use relevant English and Chinese descriptions and configuration fields. Preserve the original text separately from interpretation or translation.
- **Agreed requirement, scope control:** Compare all supplied in-scope SKUs, disclose coverage, and avoid claims about the entire CRM from a subfamily dataset. Classification errors must be disclosed, not used to justify automatic scope expansion.
- **Agreed requirement, comparison traceability:** For each requirement and SKU, show the documented value, supporting field/excerpt, assessment and outstanding question. Include the tender reference and evidence version.
- **Agreed requirement, assessment vocabulary (confirmed 2026-11-03):** `Meets`, `Does not meet`, `Not verified`, `Conflict`, and `Conditional`. Use “Not verified” for missing evidence, preserving the distinction from demonstrated failure.
- **Agreed requirement, candidate gate (confirmed 2026-11-03):** A compliant shortlist entry has no unresolved mandatory failure, missing evidence or conflict. Conditional and near-match options appear separately and do not count as compliant until resolved.
- **Agreed requirement, candidate identity (user decision, 2026-11-03):** The shortlist may contain two distinct exact SKUs of the same model or exact SKUs of different models. Model diversity is not required; each SKU must independently pass the compliance gate.
- **Agreed requirement, human control:** Keep technical assessment, engineering confirmation and commercial review visibly separate. No automatic final offer or tender submission.
- **Agreed requirement, minimized inputs:** Use reviewed technical samples and allowlisted fields; exclude credentials, signed access links, employee information and internal commercial values.

## Tender-compliance rules

- **Agreed requirement, functional boundaries:** Required functions can also define configuration limits. Additional capabilities are not automatically acceptable upgrades, and a higher-function subfamily is not an automatic substitute.
- **Agreed requirement, wording governs:** Follow the tender's wording. Do not invent prohibitions, exact-function counts, tolerances or permissions; flag ambiguity for clarification.
- **Agreed requirement, missing evidence:** Missing evidence means “not verified,” not compliant. It also does not by itself prove that the equipment fails.
- **Agreed requirement, SKU specificity:** Keep each assertion tied to the exact SKU and documented configuration. An optional accessory is not included unless the evidence establishes inclusion.
- **Agreed requirement, contradictions:** Preserve conflicting source fields, including English/Chinese differences. Do not select the more favorable statement or silently reconcile them.
- **Agreed requirement, honest shortlist:** Return fewer than two compliant candidates when necessary. Do not hide mandatory deviations inside a score or present near-matches as compliant.
- **Agreed requirement, review boundary:** Document-based assessment does not establish physical performance, certification scope, legal eligibility or engineering approval.
- **Proposed, technical interpretation checks:** Distinguish nominal values from guaranteed limits, load capacity from equipment/shipping weight, and model-registration references from actual certificate coverage. Validate this checklist with engineering.

## Approved pilot success criteria baseline

**Agreed requirement, approved baseline (user decision, 2026-11-03):** The user approved the revised staged acceptance checklist below for one real tender item as the pilot baseline and explicitly left historical corrections pending. Approval establishes acceptance criteria, not tested results; no pilot has passed them.

**Explicit scoped taxonomy disposition, owner decision 2026-11-09:** “Taxonomy readiness satisfied for the bounded Hydraulic Trolley pilot using direct category ID 3479142216177 and the existing captured dataset. Global taxonomy completeness, generalized parent-filter behavior and readiness for other categories remain unestablished.” This is a recorded scoped acceptance of the taxonomy stage, not passage of the whole checklist or evidence that unknown parent semantics have been established. The accepted route uses the exact selected child ID, not a parent-as-descendant shortcut; it relies on the verified source relationship, approved scope and existing reconciled capture. The general checklist remains the reference for other uses; this scoped disposition does not authorize another retrieval or automatically pass another stage.

The Project owner records `Pass`, `Needs correction` or `Blocked`, with supporting evidence, for each stage. Do not declare the pilot complete while a stage is unresolved; resolving a stage does not authorize the next execution step without separate authorization.

| Stage | Approved completion criterion | Required review record |
|---|---|---|
| Taxonomy readiness | Selected family/subfamily IDs, original names and parent links are checked against authorized evidence; coverage limits and whether parent filters include descendants are established. | Reviewed taxonomy extract, filter-test findings and owner scope approval. |
| Real-item interpretation | One owner-selected tender item has every mandatory requirement, functional limit and ambiguity traced to its original wording. No invented permission or restriction is used to clear a mandatory requirement. | Requirements table, clarification decisions and approved group IDs. |
| Scoped retrieval | The approved scope is accounted for by page and unique SKU ID. Missing/duplicate records and count drift are resolved or the run remains incomplete and is repeated before a complete-scope claim. | Scope record with filters, times, reported/returned/unique counts and error status. |
| Dataset fidelity and confidentiality | Every pilot record retains exact SKU/model identity and available original EN/CN technical fields; blanks and contradictions remain visible. Field and free-text review finds none of the excluded sensitive content. | Reviewed dataset, field mapping and review checklist. |
| Comparison coverage and traceability | Every supplied SKU is assessed against every mandatory requirement. Every `Meets` finding cites that SKU's source field/excerpt; unsupported findings are corrected to the appropriate non-passing status. | Requirement-by-SKU matrix and assessed-scope statement. |
| Compliance-gate checks | Reviewed real or clearly labeled synthetic examples test missing evidence, conflicting fields, extra functions, zero/one eligible result and same-model SKU variants. None produces an unsupported compliant result or cross-SKU feature transfer. Synthetic examples are not product evidence. | Expected-versus-observed checks and correction/retest record. |
| Shortlist correctness | Return zero, one or two independently qualifying exact SKUs, whether of the same or different models. Mandatory gaps, conflicts and conditional options stay outside the compliant shortlist. | Shortlist tied to the matrix, with unresolved technical questions listed separately. |
| Owner acceptance | The owner reviews the complete case, closes required corrections and explicitly accepts or rejects the pilot's usefulness and next step. Pending engineering confirmation stays labeled pending and cannot be overridden by an approval label. | Dated owner decision, outstanding limitations and separately authorized next action. |

**Agreed requirement, pilot boundary:** Successful completion would demonstrate only one reviewed case plus controlled gate checks, not catalog-wide accuracy or production readiness. Record elapsed effort and manual corrections as observations; defer numerical accuracy, throughput and latency targets until pilot evidence exists.

## Out of scope and unresolved requirements

- **Agreed requirement, current task:** Documentation only. No OKKI access, extraction, product-data retrieval, implementation or automatic restart of historical scripts.
- **Agreed requirement, initial program:** No full-catalog download per inquiry, vector database, separate ranking engine or extensive normalized technical database. Add complexity only after a validated need.
- **Proposed exclusion:** General tender discovery, distributor research, pricing optimization, automatic quotations/submissions and regulatory certification are outside the initial technical-matching pilot.
- **Agreed requirement, resolved decisions:** Same-model or different-model candidates are allowed; the compliance gate is confirmed; the Project owner is the sole approver; the revised pilot criteria are the approved baseline. These decisions do not authorize execution.
- **Open question, status eligibility:** How should inactive/disabled, customized and component-only records be handled? Source flag meanings are not verified.
- **Open question, coverage exceptions:** What controlled process should address uncategorized or misclassified products without relaxing functional boundaries?
- **Open question, pilot and governance:** Which tender item, output language, evidence-freshness rule, retention policy and sample size should be used?

The prioritized work and remaining approval questions are consolidated in `03_STATUS_AND_NEXT_STEPS.md`. Historical corrections remain pending; confirmation of the decisions above does not approve every historical statement or the document package as a whole.