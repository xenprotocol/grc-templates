# ASSET INVENTORY

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-AST-001 |
| **Version** | 1.0 |
| **Owner** | Asset Owner / ISMS Manager |
| **Approved By** | CISO |
| **Effective Date** | [______] |
| **Review Cycle** | Quarterly (or on significant change) |
| **Related** | Control A.5.9 (Inventory of information and other associated assets) |

> **Purpose:** The complete inventory of information assets and their
> owners. ISO 27001 Control A.5.9 requires identification and
> documentation of assets, owners, and classification. This is the
> foundation of the asset-based risk assessment — you cannot protect
> what you cannot find.

> **How to use this template:** one row per asset. Group by asset type
> (information, software, physical, service, people). Assign every asset
> an owner. Update on any material change; review the full inventory at
> least quarterly.

---

## 1. ASSET INVENTORY

| Asset ID | Asset Name | Asset Type | Owner | Location | Classification | Criticality (1-5) | Data Categories | Retention | Notes |
| :------- | :--------- | :--------- | :---- | :------- | :------------- | :---------------- | :-------------- | :-------- | :----- |
| AST-001 | [______] | [Information/Software/Physical/Service] | [______] | [______] | [Public/Internal/Confidential/Restricted] | [___] | [______] | [______] | [______] |
| AST-002 | [______] | [______] | [______] | [______] | [______] | [___] | [______] | [______] | [______] |
| AST-003 | [______] | [______] | [______] | [______] | [______] | [___] | [______] | [______] | [______] |

## 2. ASSET TYPES

| Type | Definition | Examples |
| :----- | :----------- | :------- |
| **Information** | Data and knowledge assets | Databases, documents, source code, credentials |
| **Software** | Applications and systems | ERP, CRM, security tools, SaaS |
| **Physical** | Hardware and facilities | Servers, laptops, network equipment, data centers |
| **Service** | Externally provided capabilities | Cloud, ISP, managed services |
| **People** | Human assets and their skills | Staff, contractors, expertise |

## 3. CLASSIFICATION SCHEME

| Classification | Definition | Handling Requirements |
| :------------- | :----------- | :--------------------- |
| **Public** | Freely disclosable | None beyond integrity |
| **Internal** | Internal use only | Access restricted to staff |
| **Confidential** | Sensitive business information | Need-to-know, encryption at rest |
| **Restricted** | Highest sensitivity (PII, secrets, IP) | Strong access control, audit logging, encryption |

## 4. INVENTORY RULES

1. Every asset has exactly one owner (A.5.9).
2. Assets are discovered via: automated discovery tools, interviews with
   process owners, review of network diagrams and system inventories.
3. Cloud assets are included (A.5.23) — shadow IT is a finding.
4. The inventory feeds the risk assessment (threat/vulnerability
   identification per asset) and the ROPA for personal data.

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **ISMS Manager** | [______] | [______] | [______] |
| **CISO** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
