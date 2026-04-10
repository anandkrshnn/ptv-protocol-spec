# PTV Protocol™ Standards Track
## Prove · Transform · Verify: Cryptographic Trust for Autonomous AI Agents

> [!IMPORTANT]
> **Institutional Notice (April 15 Pilot Readiness)**  
> This repository contains the public standards track for the PTV Protocol™. For commercial licensing, institutional healthcare pilots (April 15), and the production-hardened SDK, please follow the **[Evaluation License Request](docs/EVALUATION_LICENSE_REQUEST.md)** process.

> **Status:** 🟢 **Standards Track (Public Specification)**  
> **Maintainer:** Lead Architect | PTV Protocol (Sovereign AI Strategic Lab)  
> **IETF Draft**: [`draft-anandakrishnan-ptv-attested-agent-identity`](https://datatracker.ietf.org/doc/draft-anandakrishnan-ptv-attested-agent-identity/)  
> **Submissions**: NIST AI RMF | OECD AI Policy Observatory | UK AISI  

---

## 🚀 Executive Summary
The **PTV Protocol™** is an open specification for establishing cryptographically verifiable trust in autonomous AI agents. By anchoring agent identity in **TPM 2.0 hardware** and enforcing governance via **GAIP-2030**, PTV enables the **83/16/1 Governance Model**: automating 83% of routine decisions while securing critical outliers with human judgment.

**Verified Performance Claims** (v13.6-PARITY):
| Triage Tier | Target | Verified Mean | Use Case |
|------------|--------|--------------|----------|
| 🟢 ROUTINE | ≤5ms | **5.56ms** | Low-risk telemetry |
| 🟡 ZK_PROOF | ~187ms | **187.59ms** | Medium-risk, privacy-sensitive |
| 🔴 BFT | ~450ms | **450.52ms** | High-risk, cross-border |

---

## 📄 Documentation

- **[Technical Whitepaper v4.0](docs/whitepaper_v4.md)**: Core philosophy, mathematical foundations (ZK/BFT), and the 83/16/1 triage model.
- **[Architecture Specification](docs/ARCHITECTURE.md)**: Detailed system design and component interactions.
- **[Implementation Guide](docs/IMPLEMENTATION_GUIDE.md)**: Step-by-step instructions for building PTV-compliant agents.
- **[GAIP-2030 Governance Logic](spec/governance_logic.md)**: Technical reference for the 83/16/1 triage algorithm.
- **[Testing Strategy](docs/testing/TESTING_STRATEGY_v2.md)**: Multi-layered verification approach for production readiness.
- **[FAQ](FAQ.md)**: Frequently asked questions about tech, security, and licensing.

---

## ⚖️ Compliance Frameworks

- **[EU AI Act Mapping](docs/compliance/eu_ai_act_full_mapping.md)**: Article-by-article alignment for high-risk AI systems.
- **[NIST AI RMF Alignment](docs/compliance/nist_ai_rmf_alignment.md)**: Mapping to GOVERN, MAP, MEASURE, and MANAGE functions.
- **[HIPAA Technical Safeguards](docs/compliance/hipaa_technical_safeguards.md)**: Safeguarding PHI in healthcare AI.
- **[GDPR Privacy by Design](docs/compliance/gdpr_privacy_by_design.md)**: Article 25 implementation via ZK proofs.
- **[Traceability Matrix](spec/compliance_mapping.csv)**: 50+ row mapping to global regulatory standards.

---

## 🛠️ Working Samples

- **[Minimal Verification](samples/minimal_verification.py)**: Basic 83/16/1 triage simulation.
- **[Healthcare Federation](samples/healthcare_federation.py)**: GDPR-compliant cross-border AI training.
- **[Financial KYC](samples/financial_kyc.py)**: Multi-jurisdictional verification with BFT consensus.

---

## 🌍 The Sovereign AI Ecosystem

The PTV Protocol is the standards-track bridge of the **Sovereign AI Ecosystem**, connecting personal-scale privacy to enterprise-grade high-assurance AI.

| Repository | Scale | Target | License |
|------------|-------|--------|---------|
| **[Local Agent](https://github.com/anandkrshnn/local-agent)** | Personal | Local SLMs & Tools | MIT |
| **[PTV Protocol](https://github.com/anandkrshnn/ptv-protocol-spec)** | Standards | Regulatory Compliance | CC BY 4.0 |
| **Sovereign AI Stack** | Enterprise | High-Assurance Pilots | Commercial |

### **Learn the Principles at Personal Scale**
If you want to see how these principles (Permissions, Tool Verification, Minimal Access) work in a standalone application, check out **[Local Agent](https://github.com/anandkrshnn/local-agent)** — our open-source implementation for private, tool-calling SLMs on consumer hardware.

---

## 🤝 Engagement
We are actively seeking **Regulatory Review** and **Enterprise Pilot Partners** for Q3 2026.

- **For Regulators (NIST/OECD/AISI)**: Request private access to the reference implementation for evaluation.
- **For Enterprises**: Contact us to discuss NDA-governed pilot deployment.
- **For Researchers**: Fork this specification repo for academic analysis.

**Contact**: `ananda.krishnan@hotmail.com` | [ptv-protocol-labs](https://github.com/ptv-protocol-labs)

---

## ⚖️ Licensing & Trademarks
- **Specification**: CC BY 4.0 (Free to use, attribute required)
- **Implementation**: Proprietary (Commercial License Required)
- **Trademarks**: "PTV Protocol™", "GAIP-2030™", "Level 4™" are trademarks of Sovereign AI Strategic Lab.

*Disclaimer: This is an independent research initiative and open standard proposal. It is not affiliated with any current or past employer.*
