# AI SYSTEM CARD

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-AISC-001 |
| **Version** | 1.0 |
| **Owner** | [System Owner] |
| **Approved By** | AI Governance Board |
| **Effective Date** | [______] |
| **Review Cycle** | Annual, or on material change |
| **Related** | AI Governance Register (System ID: [______]), DPIA |

> **Purpose:** The AI System Card is the technical documentation for a single AI system. For high-risk systems it supports the EU AI Act Article 11 technical documentation obligation and the conformity assessment; for all systems it gives reviewers, auditors, and deployers a single source of truth on how the system works and where it fails.

> **How to use this template:** Complete one card per AI system before deployment. Keep evidence links live — attach test reports, model cards, and evaluation artifacts rather than summarizing them away.

---

## 1. SYSTEM OVERVIEW

| Field | Details |
| :---- | :------- |
| **System name / version** | [______] |
| **Vendor / developer** | [______] |
| **System ID (register)** | [______] |
| **AI Act risk tier** | [High / Limited / Minimal] |
| **Role in organization** | [Provider / Deployer / Both] |
| **Operational status** | [In development / in use / retired] |
| **Deployment type** | [Cloud / on-premise / edge: ______] |

## 2. INTENDED PURPOSE

2.1. **Intended purpose:** [What the system does, for whom, and in what context: ______]

2.2. **Intended users:** [______]

2.3. **Out of scope / foreseeable misuse:** [______]

2.4. **Expected deployment environments and integration points:** [______]

## 3. DATA USED

| Aspect | Description |
| :----- | :---------- |
| **Training data** | [Sources, volume, dates: ______] |
| **Validation / test data** | [______] |
| **Runtime inputs** | [______] |
| **Sensitive / special category data** | [Yes / No — which: ______] |
| **Data governance measures** | [Provenance, quality, minimization: ______] |
| **Labeling / annotation methodology** | [______] |

## 4. MODEL ARCHITECTURE AND TRAINING

4.1. **Model architecture:** [Model type, parameters, framework: ______]

4.2. **Training process:** [Training objective, fine-tuning, alignment steps: ______]

4.3. **Versioning and reproducibility:** [How models and data are versioned: ______]

4.4. **Explainability and interpretability:** [Techniques used to explain outputs, e.g., feature attribution or rationale generation: ______]

## 5. VALIDATION AND TESTING

5.1. **Evaluation results:**

| Metric | Target | Result |
| :----- | :----- | :----- |
| Accuracy | [___] | [___] |
| Precision / Recall | [___] | [___] |
| Bias / fairness metric | [___] | [___] |
| Latency / throughput | [___] | [___] |
| [Other: ______] | [___] | [___] |

5.2. **Accuracy, robustness, and cybersecurity evidence:** [Red-teaming results, adversarial testing, robustness under distribution shift, security testing per the Cyber Resilience Act where applicable: ______]

Evidence is retained with the card and includes model cards, evaluation reports, red-team logs, and penetration test results.

5.3. **External evaluation:** [Independent testing, certification, or audit results: ______]

## 6. HUMAN OVERSIGHT AND LIMITATIONS

6.1. **Human oversight design:** [Who reviews outputs, at what frequency, with what override authority: ______]

Oversight controls include automated flags, sampling rates, override procedures, and mandatory human sign-off for high-impact outputs.

6.2. **Known limitations and residual risks:** [Edge cases, failure modes, conditions where the system must not be used: ______]

Residual risks are recorded in the Risk Register and accepted by the system owner.

6.3. **Incident reporting:** [How failures are reported, per Article 73 where applicable: ______]

6.4. **Change management:** [Process for approving and documenting updates to the model, retraining triggers, and version rollback: ______]

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **System Owner** | [______] | [______] | [______] |
| **AI Governance Board** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved for use |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen, 2026). Adapt to your organization's context before use.*
