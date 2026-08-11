# Template Authoring Spec (House Style)

Every template in this repo must follow these conventions. These are
non-negotiable — they match the book "The Governance, Risk and Compliance
Architect" (Hendriksen, 2026) and auditors expect them.

## Format

- Markdown files, one template per file.
- Filename: lowercase-kebab-case (e.g., `risk-treatment-plan.md`).
- First line: `# TEMPLATE NAME (ALL CAPS TITLE)`.
- Immediately after: a Document Control table:

```
| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-XXX-001 |
| **Version** | 1.0 |
| **Owner** | [Role] |
| **Approved By** | [Role] |
| **Effective Date** | [______] |
| **Review Cycle** | [Annual/Quarterly] |
```

- Then a `> **Purpose:**` blockquote explaining what the document is for and
  who uses it.

## Section headers

- ALL-CAPS numbered sections: `## 1. PURPOSE`, `## 2. SCOPE`, etc.
- Subsections numbered `1.1`, `1.2` (markdown `###` is NOT used for
  sub-numbering; use bold text or plain numbered paragraphs).
- Use tables for structured data (never lists of key-value pairs).
- End with:

```
## APPROVAL
| Role | Name | Signature | Date |
...
## DOCUMENT CONTROL
| Version | Date | Author | Change Description |
```

- Final line: `*Template from "The Governance, Risk and Compliance Architect" (Hendriksen, 2026). Adapt to your organization's context before use.*`

## Fill-in fields

- ALWAYS use `[___]` (bracketed underscores) for fill-in blanks — never bare
  underscores (`_______`), never `[Enter ...]` style.
- Longer fields: `[______________________________]`.

## ISO 27001 accuracy (non-negotiable)

- Annex A controls referenced as **`A.5.15`** (with the A. prefix) — NEVER
  "Clause 5.15". Main body clauses keep the Clause prefix: "Clause 6.1.3".
- Main body Clauses 4-10: 4 Context, 5 Leadership, 6 Planning, 7 Support,
  8 Operation, 9 Performance evaluation, 10 Improvement.
- Annex A: 93 controls, 4 themes: 37 Organizational (A.5.x), 8 People (A.6.x),
  14 Physical (A.7.x), 34 Technological (A.8.x).
- Say **"Three Lines Model"** (IIA 2020) — never "Three Lines of Defense".
- Regulatory dates must be exact:
  - GDPR: in force 2018
  - NIS2: transposition deadline Oct 17, 2024
  - DORA: enforcement Jan 17, 2025
  - EU AI Act: in force Aug 1, 2024; prohibitions Feb 2, 2025; GPAI Aug 2,
    2025; high-risk Annex III Aug 2, 2026; Annex I Aug 2, 2027
  - Cyber Resilience Act: in force Dec 10, 2024; reporting Sep 11, 2026;
    full application Dec 11, 2027

## Voice

- Direct, practical, professional. No fluff, no marketing.
- The template is a WORKING DOCUMENT, not a lecture. Instructions to the
  user go in `> **How to use this template:**` blockquotes, not in the
  template body itself (the body is what gets filled out).
