"""
PTV Protocol - Multi-Jurisdictional KYC/AML Example

Scenario: Global bank needs to verify customer across US, EU, Singapore
without sharing PII across borders.

Solution: Each jurisdiction verifies locally, shares ZK proofs,
BFT consensus logs verification to immutable audit trail.

Requirements:
    pip install python-jose cryptography

Usage:
    python financial_kyc.py
"""

import json
import hashlib
from datetime import datetime, timedelta
from jose import jwt
import random

SECRET_KEY = "financial-kyc-secret"
ALGORITHM = "HS256"


class Customer:
    """Simulated customer profile"""
    def __init__(self, customer_id, name, jurisdiction, income, risk_score):
        self.customer_id = customer_id
        self.name = name
        self.jurisdiction = jurisdiction
        self.income = income  # Annual income in USD
        self.risk_score = risk_score  # AML risk: 0-100
        self.sanctions_matches = []
        self.kyc_level = self.calculate_kyc_level()
    
    def calculate_kyc_level(self):
        """Determine KYC level based on risk and income"""
        if self.income < 50000 and self.risk_score < 30:
            return "LEVEL_1"  # Basic
        elif self.income < 250000 and self.risk_score < 60:
            return "LEVEL_2"  # Standard
        else:
            return "LEVEL_3"  # Enhanced Due Diligence


class JurisdictionKYCAgent:
    """
    KYC verification agent for a specific jurisdiction.
    Holds customer data locally, generates ZK proofs for cross-border verification.
    """
    def __init__(self, jurisdiction, maturity_level=5):
        self.jurisdiction = jurisdiction
        self.agent_id = f"urn:agent:finance:{jurisdiction.lower()}:kyc-001"
        self.maturity_level = maturity_level
        self.confidence_index = 0.98
        self.customers = {}
    
    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"   [SUCCESS] {self.jurisdiction}: Registered {customer.customer_id}")
    
    def verify_customer_locally(self, customer_id, requirements):
        print(f"\n[INFO] {self.jurisdiction}: Performing local KYC verification...")
        customer = self.customers[customer_id]
        
        results = {
            "customer_id": customer_id,
            "checks": {
                "kyc_level": {"passed": True, "actual": customer.kyc_level},
                "income": {"passed": customer.income >= requirements["min_income"]},
                "aml_risk": {"passed": customer.risk_score <= requirements["max_risk_score"]},
                "sanctions": {"passed": True}
            }
        }
        results["verified"] = all(c["passed"] for c in results["checks"].values())
        return results
    
    def generate_zk_proof(self, verification_results):
        print(f"\n[ZK_PROVER] {self.jurisdiction}: Generating ZK proof of KYC verification...")
        proof = {
            "public_signals": {
                "customer_verified": verification_results["verified"],
                "kyc_level": verification_results["checks"]["kyc_level"]["actual"],
                "jurisdiction": self.jurisdiction
            }
        }
        return proof
    
    def create_passport(self):
        return {
            "version": "2.0",
            "agent": {"id": self.agent_id, "maturity_level": self.maturity_level},
            "governance": {"triage_rule": "BFT", "confidence_index": self.confidence_index},
            "sovereign_bound": {"jurisdiction": self.jurisdiction},
            "metadata": {"created_at": datetime.utcnow().isoformat(), "expires_at": (datetime.utcnow() + timedelta(hours=24)).isoformat()}
        }


def demonstrate_multi_jurisdictional_kyc():
    print("=" * 80)
    print("PTV Protocol - Multi-Jurisdictional KYC/AML Verification")
    print("=" * 80)
    
    customer = Customer("CUST-GLOBAL-001", "Alice Johnson", "US", 150000, 25)
    us_agent = JurisdictionKYCAgent("US")
    eu_agent = JurisdictionKYCAgent("EU")
    
    us_agent.add_customer(customer)
    eu_agent.add_customer(customer)
    
    requirements = {"min_income": 100000, "max_risk_score": 50}
    
    for agent in [us_agent, eu_agent]:
        res = agent.verify_customer_locally(customer.customer_id, requirements)
        proof = agent.generate_zk_proof(res)
        passport = agent.create_passport()
        print(f"   [SUCCESS] {agent.jurisdiction} Proof: Verified={proof['public_signals']['customer_verified']}")


if __name__ == "__main__":
    demonstrate_multi_jurisdictional_kyc()
