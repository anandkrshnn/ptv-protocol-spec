# PTV (Prove–Transform–Verify) Protocol™ & Sovereign AI Stack

**Status:** Pre‑Release / Standards Track  
**Reference:** IETF Internet‑Draft `draft-anandakrishnan-ptv-attested-agent-identity-00`  
**Author:** Anandakrishnan Damodaran (Sovereign AI Strategic Lab)

PTV is a hardware‑anchored, zero‑knowledge‑friendly governance layer for autonomous AI agents. It issues a cryptographic “digital passport” to an agent before it is allowed to act, binding model, policy, hardware, and jurisdictional context into a single attested handshake.

---

## 1. The Problem
Modern LLM and agent deployments face three structural problems:
- **Data Leakage:** Sensitive data and model IP leak across borders and vendors.
- **Identity Crisis:** No standard way to prove **which** model and **which** policy actually ran.
- **Compliance Gap:** Regulators (EU AI Act, NIST) demand evidence, but most systems only produce ad‑hoc logs.

PTV addresses this by making **every significant autonomous action** go through an attested “prove–transform–verify” flow.

---

## 2. The Solution: PTV Protocol™
At a high level, a PTV handshake:
1.  **Prove:** The agent environment proves, using TPM/TEE attestation and (optionally) Groth16‑style ZK proofs, that a specific model+policy bundle is loaded on specific hardware.
2.  **Transform:** Governance logic transforms raw attestations into a standard “digital passport” artifact.
3.  **Verify:** Verifiers (gateways, ledgers, auditors) validate the artifact before allowing execution or recording the event.

Each handshake yields a machine‑readable record suitable for compliance, incident response, and audits.

---

## 3. The 83/16/1 Rule (Governance Triage)
PTV uses an “83/16/1” governance triage pattern:
- **83%** of agent calls are auto‑approved under pre‑agreed constraints.
- **16%** are auto‑quarantined for offline review (e.g., anomalous risk, jurisdiction mismatch).
- **1%** are escalated as “Hero Handshakes” with deep evidence and human‑in‑the‑loop sign‑off.

This reflects the operational reality of high‑volume, high‑risk AI: most traffic is routine, some is suspicious, and a very small fraction is existentially important.

---

## 4. What’s in This Repository?
This repository is a **specification and reference documentation** package for PTV:
- `/docs/whitepaper_v4.md` – Conceptual breakdown (logic, math, architecture).
- `/docs/ietf-draft-link.md` – Link and metadata for the IETF Internet‑Draft.
- `/docs/architecture_diagrams/` – Diagrams of TPM 2.0 ↔ Groth16 ↔ BFT ledger flows.
- `/spec/protocol_spec.json` – The canonical JSON schema for a “Hero Handshake” artifact.
- `/spec/compliance_mapping.csv` – Mapping of PTV fields to EU AI Act obligations.
- `/samples/*` – Mock handshake logs and attestation payloads.

> 🔒 **Implementation Note:**  
> No production implementation code is included here.  
> The full reference implementation is maintained in a **separate private repository** while IP ownership, licensing, and export control reviews are finalized.  
> **Access:** Available for evaluation under NDA to regulators, cloud partners, and selected enterprises.

---

## 5. Intended Audience
- **Standards Bodies:** IETF, NIST, ENISA, OECD.
- **Regulators:** Sandbox programs and policy makers.
- **Enterprises:** Teams building sovereign AI platforms or needing hardware‑anchored governance.

For collaboration or access requests, please contact the maintainer directly.

---
*Disclaimer: This project is an independent research initiative and open standard proposal. It is not affiliated with any current or past employer.*
