# Data and Confidentiality Policy

## Never commit

- Passwords, API keys, access tokens, cookies, or session headers.
- Signed access links or temporary authenticated download URLs.
- Browser session exports or unreviewed network captures.
- Employee information, customer contacts, internal prices, or other
  confidential commercial data.
- Unreviewed OKKI exports or raw product datasets.

A private repository does not waive these exclusions.

## Evidence admitted for development

Use only reviewed, minimized samples needed for an explicitly authorized
development or validation task.

Before including a sample:

1. Confirm that sharing it in this repository is authorized.
2. Limit fields to the technical evidence needed.
3. Review structured fields and free text for sensitive content.
4. Preserve exact SKU identity and relevant original EN/CN descriptions.
5. Record provenance, scope, evidence date, and known limitations without
   retaining credentials or signed links.
6. Preserve contradictions rather than replacing them with a preferred
   interpretation.

Synthetic examples must be clearly labeled and must never be presented
as product evidence.

## Local-only material

Keep credentials, raw captures, unreviewed exports, and temporary
working data outside version control.

The .gitignore file is a convenience, not a confidentiality review.
Review every proposed commit before publishing it.

## Historical decisions

Preserve prior decisions and evidence versions during migration.
Do not silently rewrite historical findings or convert proposals into
accepted or validated behavior.