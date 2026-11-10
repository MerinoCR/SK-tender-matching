# Standing owner rules — 2026-11-10

## Authority and precedence

Owner decisions from the project conversation on 2026-11-10. This addendum supersedes contrary assessment defaults in documents 01, 02 and 03 and prior interpretation notes, only for the topics listed below. Historical findings, source requirements and test records remain unchanged. These are internal matching rules, not procurement amendments or independent engineering verification.

## Approved rules

1. Unspecified tender load means static load capacity. Compare the exact SKU's static rating. Preserve explicit dynamic or other tender bases, and missing/conflicting ratings.
2. Vascular position is equivalent to Trendelenburg under owner policy.
3. Documented bumpers imply corner placement.
4. A bottom plastic cover is sufficient for integrated oxygen/belongings storage under owner policy.
5. Wheels can always be configured as antistatic: record customization to specify, not already-installed standard compliance.
6. A documented IV-pole arrangement is treated as corner-mounted, with a polished, variable-height, same-brand pole. This does not invent mount quantity, material, inclusion or a numerical height range.
7. Insufficient or unproven backrest reach is recorded as customization to request. Retain the standard range and required mechanism; a request is not engineering confirmation or completed modification.
8. A patient trolley with back and knee adjustment is assumed to have rigid four-section construction. Apply to reviewed exact-SKU facts, not model-family inheritance.
9. Full-body X-ray is equivalent to full-length cassette travel. This rule does not establish a cassette securing system or resolve an explicit cassette-removal contradiction.
10. Detailed rail construction is not strict for application matching. Preserve tender wording and evaluate basic folding/lowering separately.
11. Fifth-wheel diameter can be tagged pending verification. Do not infer it from main-wheel size.
12. All mattresses are separate customizable products. Preserve every mattress requirement, fit condition and source conflict; do not reject the main trolley solely for mattress findings or automatically approve the final mattress.

## Design change

Use a versioned policy disposition after exact-SKU evidence review. Keep source facts, owner-rule acceptance, customization requests, verification pending, engineering confirmation and final-offer approval distinct. Explicit contradictions remain visible. Raw English/Chinese source descriptions are never overwritten by a policy inference.

The new owner_rules.py module consumes reviewed structured facts; it is not a tender parser, semantic extractor, ranking engine or final eligibility selector. The caller retains requirement references and original evidence pointers. Boolean flags must concern the same exact SKU. Unknown topics and malformed load inputs are rejected.

## Status and validation

The module and test file in this commit were executed in the response Python environment: 12 unittest methods passed, including subtests covering all twelve rules, missing facts, contradictions, explicit dynamic load, identity, input immutability and invalid values. This is a new minimal implementation, not a claim that the earlier downloadable package was committed unchanged.

The existing GitHub baseline had no pilot Python code. This commit adds a standalone policy module, not integration with the Project's existing fixed-format prototype. Existing pilot suites were not rerun; no all-SKU re-evaluation, new OKKI retrieval, engineering contact, operational matching or full-pilot acceptance occurred.

## Backlog and acceptance criteria

- Pending: reviewed migration of existing pilot code and supporting minimized inputs. No raw datasets or attachments are added here.
- Pending: integrate the policy module with packet preparation, validation and reconciliation using explicit scenario/requirement maps rather than assuming every tender has the old 35 entries.
- Pending: carry policy version and owner-rule provenance into outputs without altering immutable historical source findings.
- Pending: route mattress clauses to a separate linked configurable-product record and preserve final-fit requirements.
- Pending: run focused end-to-end integration checks and existing regressions after integration. Do not label integrated until the actual flow calls this module and preserves distinct states.
- No new compliance result is established by these unit tests. Full-offer decisions remain reviewed separately.

Run unit tests with: python -m unittest discover -s policy -p 'test_*.py' -v
