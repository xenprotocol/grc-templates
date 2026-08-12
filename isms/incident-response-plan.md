# INCIDENT RESPONSE PLAN

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-IRP-001 |
| **Version** | 1.0 |
| **Owner** | CISO / Incident Response Manager |
| **Approved By** | Management |
| **Effective Date** | [______] |
| **Review Cycle** | Annual + after every major incident |
| **Related** | Controls A.5.24-A.5.28 |

> **Purpose:** Defines how the Organization detects, responds to, contains,
> eradicates, and recovers from information security incidents. This plan
> implements the incident management controls (A.5.24-A.5.28) and supports
> regulatory reporting obligations (GDPR 72h, NIS2 24h/72h, DORA 4h/24h).

---

## 1. INCIDENT DEFINITIONS AND SEVERITY

| Severity | Definition | Examples | Response Window |
| :------- | :---------- | :------- | :-------------- |
| **Critical (S1)** | Active breach; data exfiltration; ransomware; system compromise | Ransomware, APT, mass data theft | Immediate, 24/7 escalation |
| **High (S2)** | Significant disruption; confirmed unauthorized access | Phishing with credential loss, malware outbreak | Within 2 hours |
| **Medium (S3)** | Contained incident; policy violation | Single malware detection, lost device | Within 8 hours |
| **Low (S4)** | Minor event; no impact | Phishing report, false positive | Within 24 hours |

## 2. DETECTION AND REPORTING

2.1. **Reporting channels** (all staff):

- Email: [security@______]
- Phone: [______]
- Ticketing: [______]

2.2. All staff MUST report suspected incidents without delay (A.6.8).
Never wait for confirmation — report first, classify later.

## 3. RESPONSE TEAM AND ROLES

| Role | Name | Responsibility |
| :----- | :----- | :------------- |
| **Incident Commander** | [______] | Overall coordination, decisions |
| **Technical Lead** | [______] | Containment, eradication, forensics |
| **Communications Lead** | [______] | Internal/external comms, regulatory notifications |
| **Legal** | [______] | Legal obligations, privilege, regulator liaison |
| **Business Owner** | [______] | Business continuity decisions, customer impact |

## 4. RESPONSE PHASES

### Phase 1 — Triage (S1: within 30 min)

- Confirm the incident, assign severity
- Assemble the response team
- Preserve evidence (do not delete logs, take forensic images)

### Phase 2 — Containment (S1: within 2 hours)

- Isolate affected systems (disconnect, segment)
- Preserve evidence before remediation
- Apply emergency blocks (accounts, IPs, EDR actions)

### Phase 3 — Eradication and Recovery

- Remove root cause (malware, backdoors, compromised accounts)
- Patch and harden
- Restore from verified clean backups
- Verify integrity before returning to service

### Phase 4 — Reporting and Lessons Learned

- Complete regulatory notifications on the required clocks
- Conduct post-incident review (5-Whys)
- Update controls, plans, and training
- Document the full incident record

## 5. REGULATORY AND STAKEHOLDER NOTIFICATION

| Obligation | Deadline | Trigger | Responsible |
| :---------- | :------- | :------ | :---------- |
| GDPR breach notification | 72 hours (Art. 33) | Personal data breach | DPO/Legal |
| GDPR data-subject notification | Without undue delay, where high risk (Art. 34) | Personal data breach likely to result in high risk to individuals | DPO/Legal |
| NIS2 early warning | 24 hours | Significant incident (essential/important entity) | CISO |
| NIS2 full notification | 72 hours | Same | CISO |
| DORA initial notification | 4 hours | Major ICT-related incident (financial) | CISO |
| Customers / clients | Per contract | Material impact | Business Owner |
| Insurance | Per policy | Notify within policy window | Risk Manager |

## 6. POST-INCIDENT REVIEW

6.1. Every S1/S2 incident triggers a lessons-learned review within [30]
days: what happened, what worked, what failed, and what changes prevent
recurrence. Findings feed the Corrective Action Plan process.

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **CISO** | [______] | [______] | [______] |
| **Management** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
