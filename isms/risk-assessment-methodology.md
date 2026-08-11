# RISK ASSESSMENT METHODOLOGY (RAM)

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-RAM-001 |
| **Version** | 1.0 |
| **Owner** | CISO / Risk Manager |
| **Approved By** | ISSC |
| **Effective Date** | [______] |
| **Review Cycle** | Annual |
| **Related** | Risk Register, Risk Treatment Plan, SoA |

> **Purpose:** Defines how the Organization identifies, analyzes, and
> evaluates information security risk consistently. ISO 27001:2022 Clause
> 6.1.2 requires defined risk criteria and a repeatable process. This is
> the document that makes risk assessment defensible to auditors.

---

## 1. RISK IDENTIFICATION

1.1. Risk identification is performed using an **asset-based approach**
(book Section 2.2):

- **Step 1 — Asset Inventory:** identify assets (information, systems,
  processes, people) and their owners (Control A.5.9).
- **Step 2 — Asset Classification:** classify each asset by criticality.
- **Step 3 — Threat Modeling:** identify threats to each asset (external,
  internal, accidental, environmental).
- **Step 4 — Vulnerability Identification:** identify weaknesses that
  threats could exploit.

1.2. Identification methods include: interviews with asset owners, automated
discovery tools, review of network diagrams and inventories, incident
history, and threat intelligence.

## 2. RISK ANALYSIS

2.1. Each risk is scored using the formula:

```
Risk Score = Likelihood x Impact
```

2.2. **Likelihood scale (1–5):**

| Score | Level | Definition |
| :----- | :----- | :----------- |
| 5 | Very High | Expected within the next 6 months; active exploitation observed |
| 4 | High | Likely within 12 months |
| 3 | Medium | Possible within 12–24 months |
| 2 | Low | Unlikely within 24 months |
| 1 | Very Low | Rare; not observed in similar organizations |

2.3. **Impact scale (1–5):**

| Score | Level | Definition |
| :----- | :----- | :----------- |
| 5 | Critical | Severe financial loss, regulatory action, major brand damage |
| 4 | High | Significant financial/operational impact |
| 3 | Medium | Moderate impact, containable with effort |
| 2 | Low | Minor impact, readily contained |
| 1 | Very Low | Negligible impact |

2.4. Impact is assessed across five dimensions, taking the highest:

- Confidentiality (data exposure)
- Integrity (data corruption)
- Availability (service disruption)
- Financial/Legal/Regulatory
- Reputation/Customer

## 3. RISK EVALUATION

3.1. Each risk is evaluated against the Organization's risk evaluation
criteria (book Section 2.3):

| Risk Score | Verdict | Action |
| :--------- | :------- | :------- |
| 1–4 | Acceptable | Monitor; no treatment required |
| 5–9 | Tolerable | Treatment justified; schedule action |
| 10–15 | Intolerable | Treatment mandatory; immediate action |
| 16–25 | Critical | Immediate containment; escalate to ISSC/CEO |

3.2. Evaluation criteria are reviewed annually or when risk appetite changes.

## 4. RISK TREATMENT

4.1. Treatment options (Clause 6.1.3):

| Option | Definition | Decision Factor |
| :------ | :----------- | :--------------- |
| **Mitigate** | Implement controls to reduce likelihood/impact | Control cost justified by risk reduction |
| **Transfer** | Shift risk to third party (insurance, cloud) | Third party can bear risk more efficiently |
| **Avoid** | Eliminate the activity | Risk exceeds benefit; activity not core |
| **Accept** | Documented decision to retain | Residual risk within appetite |

4.2. Selected controls map to ISO 27001 Annex A and are recorded in the
Risk Treatment Plan and the Statement of Applicability.

## 5. RESIDUAL RISK AND ACCEPTANCE

5.1. After treatment, residual risk is re-evaluated — never assumed (book
Section 2.5):

```
Residual Risk = Inherent Risk - Control Effectiveness
```

> **Auditor Note:** this formula is a practical heuristic for qualitative
> scoring. ISO 27001:2022 does not mandate a specific mathematical formula;
> it requires that residual risk is systematically evaluated and documented
> (Clause 6.1.3).

5.2. A risk is formally accepted only when: the residual score is
re-evaluated, it is within documented risk appetite, the risk owner signs
off, and evidence of reduction is documented. Use the Risk Acceptance Form.

## 6. RISK COMMUNICATION AND REPORTING

6.1. Risks are reported to stakeholders at defined intervals:

| Audience | Report | Frequency |
| :-------- | :------- | :--------- |
| Board / Executives | Executive Risk Summary | Quarterly |
| ISSC | Risk Register update | Monthly |
| Risk Owners | Treatment plan status | Monthly |
| All staff | Awareness communications | As needed |

## 7. REVIEW AND UPDATE

7.1. The full risk assessment is repeated at least annually, or when:

- Significant changes to the organization, technology, or threat landscape
- New regulations become applicable
- After major incidents
- Material changes to scope

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **Risk Manager** | [______] | [______] | [______] |
| **ISSC** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
