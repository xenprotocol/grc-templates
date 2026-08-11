# ACCESS CONTROL POLICY (Level 2)

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-ACP-001 |
| **Version** | 1.0 |
| **Owner** | CISO |
| **Approved By** | ISSC |
| **Effective Date** | [______] |
| **Review Cycle** | Annual |
| **Related Documents** | Information Security Policy [ORG]-ISP-001 (Level 1); implements Annex A controls A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 |

> **Purpose:** Level 2 policy governing how access to information and systems is granted, reviewed, and revoked. It implements the access control requirements of ISO/IEC 27001:2022 Annex A (A.5.15–A.5.18, A.8.2, A.8.3, A.8.5) and traces its authority to the Information Security Policy.
>
> **How to use this template:** Replace every `[___]` field. Keep the review cadence at least quarterly (A.8.3). Route through the ISSC for approval and reference this policy's Document ID in the Statement of Applicability.

---

## 1. PURPOSE

1.1. This policy establishes the rules for granting, managing, reviewing, and revoking access to the Organization's information and systems, to protect confidentiality, integrity, and availability (A.5.15).

## 2. SCOPE

2.1. This policy applies to all [employees, contractors, temporary staff, and third parties] accessing [systems, networks, applications, data, physical facilities] owned or operated by [ORG NAME].

## 3. ACCOUNT LIFECYCLE (A.5.16, A.5.18)

3.1. **Provisioning:** Accounts are created only upon a formal, approved access request from the resource owner. Requests identify the user, the resource, and the access level required. Default is deny; access is granted on a need-to-know basis (A.5.15).

3.2. **Changes:** Role changes, transfers, and promotions trigger an access review of the affected accounts within [5 business days].

3.3. **Deprovisioning:** On termination, access is revoked within [24 hours] of [the notice of termination]. On transfer, access to former systems is revoked within [48 hours]. Shared credentials are prohibited; every account maps to one named individual.

## 4. LEAST PRIVILEGE AND SEGREGATION OF DUTIES (A.5.15, A.5.3)

4.1. Users are granted the minimum access required for their role. Profiles are defined per role and reviewed annually.

4.2. Segregation of duties (A.5.3) is enforced for conflicting tasks — for example, a user who requests access must not also approve it; payment initiators and approvers must differ. Conflicts are identified in the access review and compensating controls documented where unavoidable.

## 5. ACCESS REVIEW (A.5.18, A.8.3)

5.1. Access rights are reviewed at least **quarterly** (A.8.3). Reviews confirm each access right is still required and appropriate.

| Review Type | Scope | Cadence | Owner |
| :---------- | :---- | :------ | :---- |
| Standard user review | All user accounts | Quarterly | [IT / Line managers] |
| Privileged review | Privileged accounts (A.8.2) | Monthly | [CISO / Security] |
| SoD conflict check | Sensitive functions | Quarterly | [Compliance] |

5.2. Review results are documented; excessive or stale rights are removed within [10 business days].

## 6. PRIVILEGED ACCESS MANAGEMENT (A.8.2)

6.1. Privileged access is granted only with ISSC- or CISO-level approval, for a stated purpose, and with a defined expiry.

6.2. Privileged accounts are: individually attributable (no shared root/admin), monitored and logged, and reviewed monthly. A privileged access management (PAM) solution is used to vault, rotate, and session-record credentials ([tool: ______]).

## 7. AUTHENTICATION (A.5.17, A.8.5)

7.1. Authentication information is never shared or written down; initial passwords are unique, and forced change is enforced at first login (A.5.17).

7.2. Multi-factor authentication (MFA) is required for: all remote access, all privileged access, and all access to [critical systems: ______] (A.8.5).

7.3. Password rules follow [the Organization's password standard]: minimum [12] characters, [MFA where available], and [lockout after 5 failed attempts].

## 8. REMOTE ACCESS

8.1. Remote access is permitted only through the approved channel [VPN / zero-trust gateway: ______] with MFA, per this policy and the Remote Access Procedure.

8.2. The remote access solution is patched and logged; remote sessions are subject to the same access reviews as on-site access.

## 9. EXCEPTIONS

9.1. Any deviation from this policy requires a documented Policy Exception Request ([ORG]-EXC-001), including compensating controls, a risk assessment, and ISSC approval for critical exceptions.

## 10. ENFORCEMENT AND REVIEW

10.1. Non-compliance is reported to the CISO and may be escalated to the ISSC and HR as appropriate.

10.2. This policy is reviewed annually or upon significant change (Clause 7.5); changes are approved by the ISSC.

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **CISO / Policy Owner** | [______] | [______] | [______] |
| **ISSC Chair** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved by ISSC |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen, 2026). Adapt to your organization's context before use.*
