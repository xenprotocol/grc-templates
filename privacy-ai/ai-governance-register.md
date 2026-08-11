# AI GOVERNANCE REGISTER

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-AIGR-001 |
| **Version** | 1.0 |
| **Owner** | Head of AI Governance / CISO |
| **Approved By** | AI Governance Board |
| **Effective Date** | [______] |
| **Review Cycle** | Quarterly |
| **Related** | AI System Cards, AI Acceptable Use Policy, ROPA |

> **Purpose:** The AI Governance Register is the organization's inventory of all AI systems in use, including shadow AI discovered during reviews. It records each system's EU AI Act risk tier and is the foundation for the obligations the organization must meet as provider, deployer, or both.

> **How to use this template:** Register every AI system — procured, built, or embedded in third-party products. Classify risk tier at onboarding and re-classify on material change. EU AI Act (in force Aug 1, 2024) obligations apply progressively: prohibitions Feb 2, 2025; GPAI Aug 2, 2025; high-risk Annex III Aug 2, 2026; Annex I Aug 2, 2027.

---

## 1. RISK TIER DEFINITIONS

1.1. Classification follows the EU AI Act risk tiers:

| Tier | Definition | Examples |
| :--- | :--------- | :------- |
| **Unacceptable** | Prohibited practices (Art. 5) | Social scoring, manipulative subliminal techniques |
| **High** | Annex I or Annex III systems | Recruitment screening, credit scoring, biometric ID |
| **Limited** | Transparency obligations (Art. 50) | Chatbots, deepfakes, emotion recognition |
| **Minimal** | No specific obligations | Spam filters, games |

## 2. AI SYSTEM REGISTER

2.1. One row per AI system:

| System ID | System Name | Vendor / Developer | Description | Risk Tier | Annex III Category (if high) | Role | AIQ Score | ABR Score | Owner | Status | Next Review |
| :-------- | :---------- | :----------------- | :---------- | :-------- | :--------------------------- | :--- | :-------- | :-------- | :---- | :----- | :---------- |
| AI-001 | [______] | [______] | [______] | [High] | [Annex III point 4 — employment] | [Provider / Deployer / Both] | [___] | [___] | [______] | [In use / pilot / retired] | [______] |
| AI-002 | [______] | [______] | [______] | [___] | [___] | [___] | [___] | [___] | [______] | [______] | [______] |

2.2. **AIQ (AI Quality) score** reflects the system's quality, accuracy, and robustness assessment; **ABR (AI Business Risk) score** reflects business and compliance exposure. Both are scored 1–5 using the AI risk assessment methodology: [reference: ______]

2.3. **High-risk obligations by role** (recorded per system in the RACI matrix):

- **Provider:** risk management system, data governance, technical documentation (Art. 11), log-keeping, transparency, human oversight, accuracy/robustness/cybersecurity.
- **Deployer:** use per instructions, human oversight, monitoring, incident reporting, transparency to affected persons.

2.4. **Limited-tier systems** (Art. 50) are recorded with their transparency measures: user notification, labeling of AI-generated content, and disclosure to affected persons. **Unacceptable-tier practices** (Art. 5) are prohibited outright; any discovered use is escalated for immediate remediation.

## 3. REVIEW AND CHANGE MANAGEMENT

3.1. The register is reviewed quarterly. Material changes (new capability, new data, role change, vendor change) trigger re-classification within [30] days.

3.2. Systems found in use but not registered (shadow AI) are added immediately, classified, and assessed for remediation or removal.

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **Head of AI Governance** | [______] | [______] | [______] |
| **AI Governance Board** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved for use |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen, 2026). Adapt to your organization's context before use.*
