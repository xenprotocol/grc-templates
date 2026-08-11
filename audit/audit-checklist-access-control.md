# ACCESS CONTROL AUDIT CHECKLIST

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-ACAC-001 |
| **Version** | 1.0 |
| **Auditor** | [______] |
| **Audit Date** | [______] |
| **Related** | Controls A.5.15-A.5.18, A.8.2, A.8.3, A.8.5 |

> **Purpose:** Field checklist for auditing access control. Tests the
> access control controls (A.5.15-A.5.18 identity/authentication/access
> rights, A.8.2 privileged access, A.8.3 information access restriction,
> A.8.5 secure authentication) with concrete verification steps.

> **How to use this template:** work through each check, record evidence
> (config exports, screenshots, interview notes), and mark the result.
> "Sample" checks require testing a representative sample (e.g., 10
> access reviews, 5 terminations).

---

## 1. POLICY AND PROCESS

- [ ] Access control policy exists and is current (A.5.15)
- [ ] Roles and responsibilities for access management defined
- [ ] Access review process defined and documented
- [ ] Account lifecycle process defined (provision, change, revoke)

## 2. IDENTITY AND AUTHENTICATION (A.5.16, A.5.17, A.8.5)

- [ ] Unique user IDs for all accounts (no shared accounts without justification)
- [ ] MFA enforced for privileged and remote access
- [ ] Password policy enforced (length, complexity, rotation)
- [ ] Default passwords changed on all systems
- [ ] Authentication information stored securely (hashed, never plaintext)
- [ ] Inactive accounts disabled after [90] days

## 3. ACCESS RIGHTS (A.5.18, A.8.3)

- [ ] Least privilege applied — rights match role requirements
- [ ] Access reviews completed per schedule (sample: [___] of [___] reviews)
- [ ] Terminations: access revoked within [24] hours (sample: [___] of [___])
- [ ] Transfers: access adjusted to new role (sample: [___] of [___])
- [ ] Temporary access has expiry dates

## 4. PRIVILEGED ACCESS (A.8.2)

- [ ] Privileged accounts inventoried and owners assigned
- [ ] Privileged access requires MFA
- [ ] Privileged activity logged and monitored
- [ ] Standing privileges reviewed quarterly
- [ ] Break-glass / emergency access process documented and tested

## 5. TECHNICAL VERIFICATION

- [ ] Directory query: no orphaned accounts in [system: ______]
- [ ] Admin group membership matches authorized list (sample: [___] of [___])
- [ ] Failed-login monitoring active and alerting
- [ ] Remote access requires MFA + VPN/ZTNA
- [ ] Segregation of duties enforced for [high-risk functions: ______]

## 6. FINDINGS SUMMARY

| Ref | Finding | Severity | Requirement |
| :--- | :------ | :------- | :---------- |
| [______] | [______] | [Major/Minor/Observation] | [A.5.18 / ______] |

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **Auditor** | [______] | [______] | [______] |
| **Auditee** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
