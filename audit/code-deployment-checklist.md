# CODE DEPLOYMENT CHECKLIST

| Field | Details |
| :----- | :------- |
| **Document ID** | [ORG]-CDC-001 |
| **Version** | 1.0 |
| **Owner** | Release Manager / DevOps Lead |
| **Approved By** | [CISO / Engineering Manager] |
| **Effective Date** | [______] |
| **Related** | Controls A.8.25-A.8.32 (Secure development, change management) |

> **Purpose:** Pre-deployment gate for code changes to production.
> Implements secure development lifecycle controls (A.8.25-A.8.32):
> every deployment must pass these checks before release. This is the
> "build-blocking policy" made concrete.

> **How to use this template:** attach to every release ticket. All
> mandatory checks must pass (or have documented, approved exceptions)
> before deployment. The release manager signs off.

---

## 1. CHANGE IDENTIFICATION

| Field | Value |
| :----- | :------ |
| **Change/Release ID** | [CHG-2026-___] |
| **Application/System** | [______] |
| **Change Description** | [______] |
| **Risk Classification** | [Low / Medium / High / Critical] |
| **Deployment Window** | [______] |

## 2. MANDATORY CHECKS

### Security

- [ ] Security review completed (SAST/DAST results reviewed, no critical findings)
- [ ] No secrets/credentials in code or config (secret scanning clean)
- [ ] Dependencies scanned for known vulnerabilities (no critical CVEs)
- [ ] OWASP Top 10 / [standard] check applied to changes
- [ ] Authentication/authorization changes reviewed (A.8.2, A.8.3)
- [ ] Logging and monitoring requirements met (A.8.15, A.8.16)

### Process

- [ ] Code review completed by [peer / senior reviewer]
- [ ] Tests passed (unit, integration, regression) in CI/CD
- [ ] Change approved via [change management process]
- [ ] Rollback plan documented and tested
- [ ] Documentation updated (runbooks, architecture)

### Compliance

- [ ] Compliance-as-code checks passed (policy gates, if applicable)
- [ ] Data protection review complete (if personal data affected) (A.8.10)
- [ ] Third-party components approved (SBOM updated where applicable)

## 3. DEPLOYMENT EXECUTION

| Field | Value |
| :----- | :------ |
| **Deployed By** | [______] |
| **Deployment Time** | [______] |
| **Version Tag** | [______] |
| **Post-deployment verification** | [Health checks, smoke tests: ______] |

## 4. EXCEPTIONS

| Check | Exception Reason | Approved By | Expiry |
| :---- | :--------------- | :---------- | :----- |
| [______] | [______] | [______] | [______] |

## 5. SIGN-OFF

| Role | Name | Signature | Date |
| :----- | :----- | :--------- | :----- |
| **Developer** | [______] | [______] | [______] |
| **Reviewer** | [______] | [______] | [______] |
| **Release Manager** | [______] | [______] | [______] |

---

## DOCUMENT CONTROL

| Version | Date | Author | Change Description |
| :------ | :----- | :------ | :------------------ |
| 0.1 | [______] | [______] | Initial draft |
| 1.0 | [______] | [______] | Approved |

---

*Template from "The Governance, Risk and Compliance Architect" (Hendriksen,
2026). Adapt to your organization's context before use.*
