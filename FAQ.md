# Frequently Asked Questions (FAQ)
## PTV Protocol v2.0

**Last Updated:** April 2026

---

## General Questions

### Q1: What is PTV Protocol?
**A:** PTV (Prove-Transform-Verify) is an **open specification** for establishing cryptographically verifiable trust in AI agents. It enables AI systems to prove compliance with regulations (EU AI Act, GDPR, HIPAA) without exposing sensitive data.

### Q2: Why do I need PTV?
**A:** Traditional AI frameworks rely on self-certification. PTV provides **cryptographic proof** of compliance, making it suitable for regulated industries like healthcare and finance.

---

## Technical Questions

### Q3: What are the performance benchmarks?
- **ROUTINE**: ~5ms (Hash check)
- **ZK_PROOF**: ~187ms (Groth16 generation)
- **BFT**: ~450ms (Consensus overhead)

### Q4: Is a TPM required?
**A:** For production, **YES**. Hardware-anchored identity (TPM 2.0) is essential for cryptographic trust. For development, a software simulator is acceptable.

---

## Compliance Questions

### Q5: Does PTV satisfy the EU AI Act?
**A:** Yes. It provides technical implementations for Articles 10, 13, 14, 15, and 50 of the EU AI Act.

---

*This FAQ is continuously updated based on community questions.*  
*Last updated: April 10, 2026*
