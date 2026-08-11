# OT SECURITY READINESS CHECKLIST

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-OT-CHK-001 |
| **Version** | 1.0 |
| **Owner** | [OT Security Lead] |
| **Approved By** | [CISO / Operations Director] |
| **Effective Date** | [______] |
| **Review Cycle** | Annual (and after major OT changes) |
| **Next Review Date** | [______] |
| **Classification** | Internal |

> **Purpose:** Self-assessment of OT security readiness, aligned to IEC 62443
> and the Purdue model. Completed by the OT security lead with plant
> operations, reviewed with the CISO. "No" answers become inputs to the
> OT remediation plan.

---

## 1. ASSET INVENTORY

- [ ] Complete OT asset inventory exists (hardware, firmware, network)
- [ ] Inventory records firmware versions, patch status, and EOL/EOS dates
- [ ] Inventory is verified against the live network [quarterly / on change]

## 2. ZONING AND SEGMENTATION (PURDUE MODEL)

- [ ] All assets assigned to zones and conduits per IEC 62443-3-2
- [ ] Zone boundaries enforced by [firewalls / ACLs: ______]
- [ ] No direct L0-L2 to L4/L5 connections without crossing the DMZ

## 3. INDUSTRIAL DMZ (IT/OT SEGMENTATION)

- [ ] All IT/OT traffic flows through an industrial DMZ (L3.5)
- [ ] No direct IT-to-OT or OT-to-IT connections exist
- [ ] DMZ devices are hardened, monitored, and patched

## 4. REMOTE ACCESS

- [ ] Remote access requires MFA (e.g., [______])
- [ ] Remote access is jump-host based through the DMZ, not direct to assets
- [ ] Remote sessions are logged, monitored, and time-limited

## 5. PATCH MANAGEMENT

- [ ] Risk-based OT patch policy approved (IEC 62443-2-1)
- [ ] Security Patch Remediation Status (SP1-SP4) assigned per asset
- [ ] Vendor-approved patching windows defined and tested

## 6. INCIDENT RESPONSE

- [ ] OT-specific incident response playbook exists and is tested
- [ ] IR team trained on OT protocols and safety constraints
- [ ] OT logs (SCADA, controllers, DMZ) flow to a central SIEM

## 7. SAFETY INTEGRATION

- [ ] Safety Instrumented Systems (SIS) identified and segregated
- [ ] Change management assesses safety impact of every change
- [ ] Safety functions remain operable during cybersecurity incidents

## 8. IEC 62443 ASSESSMENT STATUS

- [ ] Target Security Level (SL) defined per zone
- [ ] Gap assessment performed (IEC 62443-3-2 / -2-1)
- [ ] Remediation plan approved, funded, and tracked

> **How to use this template:** Mark each item [Yes/No/Partial] in
> [______]. Score = [___] of [___] complete. Unchecked items feed the
> OT remediation plan with owners and target dates; revisit at least
> annually and after any zoning or architecture change.

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **OT Security Lead** | [______] | [______] | [______] |
| **Plant / Operations Manager** | [______] | [______] | [______] |
| **CISO** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved for release |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen, 2026). Adapt to your organization's context before use.*
