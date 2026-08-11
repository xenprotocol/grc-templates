# GRC Architect — Companion Template Repository

Production-grade, fill-and-modify templates for **"The Governance, Risk and
Compliance Architect: Building Resilient Frameworks for the AI Era"** by
Thomas Hendriksen (xenprotocol), First Edition (2026).

Every template follows the book's conventions: ISO 27001:2022 Annex A control
numbering (A.X.XX), exact regulatory dates, the IIA Three Lines Model, and
fill-in fields marked with `[___]` brackets. Adapt each template to your
organization's context — never deploy a template unmodified.

## Quick Start

1. Clone or download this repository.
2. Open the `README.md` inside each domain folder for the template index and
   usage notes.
3. Copy a template, replace every `[___]` field, and route it through your
   normal document control (version, owner, approval).

## Structure

```
grc-templates/
├── isms/            Core ISMS suite (ISO 27001:2022)
│   ├── information-security-policy.md
│   ├── isms-scope.md
│   ├── statement-of-applicability.md
│   ├── risk-assessment-methodology.md
│   ├── risk-register.md
│   ├── risk-treatment-plan.md
│   ├── risk-acceptance-form.md
│   ├── internal-audit-procedure.md
│   ├── internal-audit-report.md
│   ├── management-review-minutes.md
│   ├── incident-response-plan.md
│   ├── supplier-security-assessment.md
│   └── business-continuity-policy.md
├── governance/      Governance bodies and policy lifecycle
│   ├── issc-charter.md
│   ├── issc-meeting-minutes.md
│   ├── policy-exception-request.md
│   ├── information-security-policy-tier2-example.md
│   └── governance-readiness-checklist.md
├── risk/            Risk management artifacts
│   ├── asset-inventory.md
│   ├── risk-assessment-worksheet.md
│   ├── executive-risk-summary.md
│   └── risk-communication-template.md
├── audit/           Audit lifecycle artifacts
│   ├── internal-audit-plan.md
│   ├── audit-checklist-access-control.md
│   ├── corrective-action-plan.md
│   └── code-deployment-checklist.md
├── privacy-ai/      Privacy, data protection, and AI governance
│   ├── ropa.md
│   ├── dpia.md
│   ├── retention-policy.md
│   ├── ai-governance-register.md
│   ├── ai-system-card.md
│   ├── ai-acceptable-use-policy.md
│   └── ai-provider-deployer-raci.md
├── resilience/      Operational resilience and business continuity
│   ├── bia-one-page.md
│   ├── press-statement.md
│   └── third-party-exit-strategy.md
├── ot/              Operational technology (IEC 62443)
│   ├── ot-asset-inventory.md
│   └── ot-security-readiness-checklist.md
├── checklists/      Cross-cutting checklists
│   ├── management-review-inputs.md
│   ├── first-90-days-governance.md
│   ├── security-champion-charter.md
│   └── human-risk-90-day-plan.md
└── README.md        This file
```

## License

MIT — see [LICENSE](LICENSE). Templates are free to use, adapt, and
redistribute for internal organizational use. The book itself is a separate
copyrighted work.

## Verification

- All templates use `[___]` for fill-in fields (LaTeX-safe, book convention).
- Annex A controls referenced as `A.X.XX` (never "Clause 5.15").
- Regulatory dates match the book's verified enforcement dates.
- "Three Lines Model" (IIA 2020), never "Three Lines of Defense".
