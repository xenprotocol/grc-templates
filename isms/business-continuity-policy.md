# BUSINESS CONTINUITY POLICY

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-BCP-001 |
| **Version** | 1.0 |
| **Owner** | Business Continuity Manager |
| **Approved By** | Management |
| **Effective Date** | [______] |
| **Review Cycle** | Annual |
| **Related** | Controls A.5.29, A.5.30, A.8.14 |

> **Purpose:** Defines the Organization's approach to business continuity:
> continuity objectives, tolerances, responsibilities, and the testing
> program. Implements A.5.29 (information security during disruption) and
> A.5.30 (ICT readiness for business continuity), and supports DORA/NIS2
> resilience obligations where applicable.

---

## 1. POLICY STATEMENT

1.1. The Organization maintains the capability to continue critical
business functions during and after disruptive events.

1.2. Continuity objectives are defined in terms of:

| Tolerance | Definition | Target |
| :-------- | :---------- | :----- |
| **MTD** (Maximum Tolerable Downtime) | Longest a function can be impaired before damage is unacceptable | [24] hours for critical functions |
| **RTO** (Recovery Time Objective) | Target time to restore after disruption | [12] hours |
| **RPO** (Recovery Point Objective) | Maximum acceptable data loss | [4] hours |
| **IPO** (Maximum Information Processing Outage) | Longest information processing can be unavailable | [24] hours |

## 2. SCOPE AND CRITICAL FUNCTIONS

2.1. Business Impact Analyses are performed for all business functions to
determine criticality and tolerances (see BIA template).

2.2. Critical functions are reviewed at least annually:

| Critical Function | MTD | RTO | RPO | Owner |
| :---------------- | :-- | :-- | :-- | :---- |
| [______] | [___] | [___] | [___] | [______] |
| [______] | [___] | [___] | [___] | [______] |

## 3. CONTINUITY STRATEGY

3.1. The Organization's strategies include:

- **Redundancy:** critical systems have redundant capacity (A.8.14)
- **Backups:** regular verified backups meeting RPO targets (A.8.13)
- **Alternate sites:** [warm/cold site arrangements: ______]
- **Vendor redundancy:** critical third parties have exit strategies

## 4. TESTING AND EXERCISING

4.1. Continuity arrangements are tested at least annually:

| Test Type | Frequency | Method |
| :-------- | :-------- | :----- |
| **Backup restoration test** | Monthly | Restore from backup, verify integrity |
| **Tabletop exercise** | Quarterly | Scenario walkthrough with management |
| **Full failover test** | Annual | Switch to alternate site/DR environment |

4.2. Test results are documented, findings tracked to closure, and
reported to management (input to Clause 9.3).

## 5. ACTIVATION AND RESPONSIBILITIES

5.1. The Business Continuity Plan is activated by the Incident Commander
when a disruption exceeds [defined trigger: e.g., 4 hours or critical
function loss].

5.2. Roles:

| Role | Responsibility |
| :----- | :------------- |
| **Incident Commander** | Activation decision, coordination |
| **BC Manager** | Plan execution, recovery coordination |
| **Communications** | Stakeholder and customer updates |
| **IT Operations** | Technical recovery, restoration |

## 6. REVIEW

6.1. This policy is reviewed annually, after major disruptions, and when
the business changes materially (new critical functions, new locations,
outsourcing changes).

---

## APPROVAL

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **BC Manager** | [______] | [______] | [______] |
| **Management** | [______] | [______] | [______] |

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
