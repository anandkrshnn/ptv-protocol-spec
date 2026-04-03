# 🎛️ GAIP-2030 Governance Framework (v2.0)

## Overview
GAIP-2030 (Governance, Attestation, Identity, Policy) is the policy engine that powers the PTV Protocol™. It enables dynamic, risk-based governance for autonomous AI agents through the **83/16/1 Triage Rule** and **Confidence Index** scoring.

---

## 🔄 The 83/16/1 Triage Rule

Every agent request is evaluated and routed to one of three verification tiers:

| Tier | Distribution | Verification Method | Latency | Use Case |
|------|-------------|-------------------|---------|----------|
| **🟢 ROUTINE** | 83% | Hash check only | ≤5ms | Low-risk telemetry, non-sensitive data |
| **🟡 ZK_PROOF** | 16% | Full Groth16 proof | ~187ms | Medium-risk decisions, PHI/PII handling |
| **🔴 BFT** | 1% | 3/5 node consensus | ~450ms | High-risk, irreversible, cross-border actions |

### Triage Decision Logic
\\\python
if risk_score < 0.7:
    tier = "ROUTINE"    # Hash verification only
elif risk_score < 0.95:
    tier = "ZK_PROOF"   # Full zero-knowledge proof
else:
    tier = "BFT"        # Byzantine fault-tolerant consensus
\\\

**Risk Factors Evaluated:**
- Data sensitivity (PHI, PII, financial)
- Transaction value/impact
- Cross-jurisdictional boundaries
- Irreversibility of action
- Agent maturity level

---

## 📊 Post-Application-Era Maturity Levels

Agents declare their operational maturity, which influences verification requirements:

| Level | Name | Requirements | Confidence Index Min |
|-------|------|-------------|---------------------|
| **1** | Initial | Software anchor, basic attestation | None |
| **2** | Managed | Hardware anchor, manual compliance | ≥0.70 |
| **3** | Defined | TPM/TEE anchor, policy enforcement | ≥0.80 |
| **4** | Quantitative | TPM 2.0 + ZK-proofs + statistical monitoring | **≥0.95** |
| **5** | Optimizing | Cross-border autonomy + BFT audit + self-improvement | **≥0.99** |

### Maturity Progression Criteria
An agent advances levels by demonstrating:
1. **Consistent compliance** with declared policies
2. **Verifiable hardware anchoring** (TPM/TEE)
3. **Statistical reliability** (confidence index trends)
4. **Successful audit outcomes** (zero critical findings)

---

## 🎯 Confidence Index (0.0-1.0)

The Confidence Index is a statistical measure of trust in an agent's decision:

**Calculation Factors:**
- Historical accuracy rate
- Policy compliance consistency
- Hardware attestation freshness
- Peer validation scores (for BFT tier)

**Usage in Triage:**
- Confidence ≥0.95 + Level 4+ → Eligible for ROUTINE tier escalation
- Confidence <0.80 → Automatic downgrade to ZK_PROOF or BFT tier
- Confidence <0.50 → Mandatory human review regardless of risk score

---

## 🌍 Sovereign Bound Enforcement

The \sovereign_bound\ block ensures jurisdictional compliance:

\\\json
"sovereign_bound": {
  "jurisdiction": "EU/DE",
  "compliance": ["GDPR", "EU_AI_ACT", "HIPAA"],
  "data_residency": "eu-central-1"
}
\\\

**Verification Rules:**
- Requests crossing jurisdiction boundaries trigger automatic ZK_PROOF tier
- Data residency mismatches result in immediate rejection
- Compliance declarations must match active regulatory frameworks

---

## 📋 Compliance Mapping (EU AI Act)

| GAIP-2030 Control | EU AI Act Article | PTV Passport Field |
|------------------|------------------|-------------------|
| Risk Assessment | Art. 15(1) | \governance.triage_rule\ |
| Data Governance | Art. 10 | \sovereign_bound.data_residency\ |
| Transparency | Art. 50 | \gent.maturity_level\ + \ttestation.proof\ |
| Human Oversight | Art. 14 | \governance.human_override\ |
| Accuracy/Robustness | Art. 15(4) | \governance.confidence_index\ |
| Technical Documentation | Annex IV | Entire Passport v2.0 schema |

> **Note:** This framework is designed for regulatory review. Implementations must undergo third-party validation for formal compliance certification.
