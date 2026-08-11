# OT ASSET INVENTORY (IEC 62443 / PURDUE)

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-OT-INV-001 |
| **Version** | 1.0 |
| **Owner** | [OT Security Lead / Plant Manager] |
| **Approved By** | [CISO / Operations Director] |
| **Effective Date** | [______] |
| **Review Cycle** | Quarterly (or on change) |
| **Next Review Date** | [______] |
| **Classification** | Internal |

> **Purpose:** Asset inventory for operational technology (OT), organized by
> Purdue model level and IEC 62443 zone/conduit. It is the baseline for
> patch management (IEC 62443-2-1), vulnerability management, zoning
> (IEC 62443-3-2), and OT risk assessment. Maintained by the OT security
> team; verified against the network by [asset discovery tool: ______].

---

## 1. ASSET REGISTER

| Asset ID | Device Type | Manufacturer / Model | Firmware Version | Purdue Level | Zone | Conduit | Function | Criticality | Patch Status | EOL / EOS | Owner |
| :------- | :---------- | :------------------- | :--------------- | :----------- | :--- | :------ | :------- | :---------- | :----------- | :-------- | :---- |
| [OT-XXX] | [PLC / HMI / RTU / Historian / Server / Switch] | [______] | [______] | [L0-L4] | [Zone 01] | [C-01] | [______] | [Critical / High / Medium / Low] | [SP1 / SP2 / SP3 / SP4 / EOL] | [______] | [______] |
| [OT-XXX] | [______] | [______] | [______] | [______] | [______] | [______] | [______] | [______] | [______] | [______] | [______] |

## 2. ZONE AND CONDUIT CONVENTIONS

| Purdue Level | Description | Typical Assets |
| :----------- | :---------- | :------------- |
| L0 | Process | Sensors, actuators, field devices |
| L1 | Basic Control | PLCs, RTUs, DCS controllers |
| L2 | Area Supervisory | HMIs, SCADA servers |
| L3 | Site Operations | Historians, asset management |
| L3.5 | Industrial DMZ | Jump hosts, proxies, patching servers |
| L4 | Enterprise | ERP, business systems |

Zones group assets with shared security requirements; conduits are the
communication paths between zones. Every asset is assigned one zone and
one or more conduits in accordance with IEC 62443-3-2.

## 3. ASSET ID CONVENTION

| Prefix | Device Type |
| :----- | :---------- |
| [PLC-] | [Programmable Logic Controller] |
| [HMI-] | [Human-Machine Interface] |
| [RTU-] | [Remote Terminal Unit] |
| [SRV-] | [Server / Historian] |
| [NET-] | [Network device] |
| [______] | [______] |

## 4. PATCH AND SUPPORT STATUS CONVENTIONS

| Status | Meaning |
| :----- | :------ |
| **SP1** | Critical / internet-facing — patch immediately |
| **SP2** | High risk — patch within [___] days |
| **SP3** | Medium risk — patch within [___] days |
| **SP4** | Low risk — patch within [___] days |
| **EOL** | End-of-life — mitigation in place: [______] |

> **How to use this template:** One row per asset, including virtualized
> and network infrastructure. Confirm firmware and patch status at each
> maintenance window. Assets at EOL/EOS require a documented mitigation or
> replacement plan before the next risk assessment.

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
