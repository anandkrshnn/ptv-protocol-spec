"""
PTV Protocol - Minimal Verification Example

Demonstrates the core concept: creating and verifying a Digital Passport
using the 83/16/1 triage model.

Requirements:
    pip install python-jose cryptography

Usage:
    python minimal_verification.py
"""

import json
import hashlib
from datetime import datetime, timedelta
from jose import jwt

# Mock constants (in production, these come from TPM 2.0)
AGENT_HARDWARE_ID = "TPM-2.0-EK-SHA256:abc123def456..."
SECRET_KEY = "your-secret-key-here"  # In production: from TPM
ALGORITHM = "HS256"


def create_digital_passport(agent_id, maturity_level, confidence_index):
    """
    Create a minimal Digital Passport (v2.0)
    
    In production, this includes:
    - TPM 2.0 attestation quote
    - Groth16 ZK proof (if ZK_PROOF tier)
    - BFT validator signatures (if BFT tier)
    """
    passport = {
        "version": "2.0",
        "agent": {
            "id": agent_id,
            "name": f"Agent {agent_id}",
            "hardware_id": AGENT_HARDWARE_ID,
            "maturity_level": maturity_level
        },
        "governance": {
            "triage_rule": "ROUTINE",  # Will be determined by broker
            "confidence_index": confidence_index,
            "policy_version": "GAIP-2030-v1.2"
        },
        "sovereign_bound": {
            "jurisdiction": "US",
            "data_residency": "us-east-1",
            "compliance": {
                "gdpr": False,
                "hipaa": True
            }
        },
        "metadata": {
            "created_at": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(hours=24)).isoformat(),
            "nonce": hashlib.sha256(str(datetime.utcnow().timestamp()).encode()).hexdigest()[:16]
        }
    }
    return passport


def calculate_risk_score(data_type, operation, cross_border=False):
    """
    Calculate risk score for a request.
    
    Factors:
    - Data sensitivity (40%)
    - Transaction value (30%)
    - Cross-border (20%)
    - Agent history (10%)
    """
    sensitivity_scores = {
        "PUBLIC": 0.0,
        "INTERNAL": 0.3,
        "CONFIDENTIAL": 0.6,
        "PII": 0.8,
        "PHI": 1.0
    }
    
    operation_scores = {
        "READ": 0.2,
        "LIST": 0.2,
        "CREATE": 0.5,
        "UPDATE": 0.6,
        "DELETE": 0.9
    }
    
    data_sensitivity = sensitivity_scores.get(data_type, 0.5)
    operation_risk = operation_scores.get(operation, 0.5)
    jurisdiction_crossing = 1.0 if cross_border else 0.0
    
    risk_score = (
        0.40 * data_sensitivity +
        0.30 * operation_risk +
        0.20 * jurisdiction_crossing +
        0.10 * 0.0  # Agent history (0.0 = good history)
    )
    
    return risk_score


def determine_triage_tier(passport, risk_score):
    """
    Apply 83/16/1 triage logic.
    
    Returns: "ROUTINE", "ZK_PROOF", "BFT", or "REJECT"
    """
    confidence = passport["governance"]["confidence_index"]
    maturity = passport["agent"]["maturity_level"]
    
    # Low risk + high confidence → ROUTINE
    if risk_score < 0.3 and confidence >= 0.95:
        return "ROUTINE"
    
    # Medium risk + acceptable confidence → ZK_PROOF
    elif risk_score < 0.7 and confidence >= 0.70:
        return "ZK_PROOF"
    
    # High risk + sufficient maturity → BFT
    elif maturity >= 4 and confidence >= 0.70:
        return "BFT"
    
    # Otherwise → REJECT
    else:
        return "REJECT"


def sign_passport(passport):
    """
    Sign the passport with JWT (simplified version)
    """
    token = jwt.encode(passport, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_passport(token):
    """
    Verify a Digital Passport
    """
    try:
        passport = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Check expiry
        expires_at = datetime.fromisoformat(passport["metadata"]["expires_at"])
        if datetime.utcnow() > expires_at:
            return False, None, "Passport expired"
        
        # Check maturity level requirement for tier
        tier = passport["governance"]["triage_rule"]
        maturity = passport["agent"]["maturity_level"]
        
        if tier == "BFT" and maturity < 4:
            return False, None, "BFT tier requires maturity level 4+"
        
        # Check confidence threshold
        if passport["governance"]["confidence_index"] < 0.70:
            return False, None, "Confidence below minimum 0.70"
        
        return True, passport, "Valid passport"
    except Exception as e:
        return False, None, f"Verification error: {str(e)}"


def demonstrate_83_16_1_triage():
    print("=" * 70)
    print("PTV Protocol 83/16/1 Triage Demonstration")
    print("=" * 70)
    print()
    
    # Scenario 1: Low-risk telemetry (ROUTINE)
    passport_routine = create_digital_passport("urn:agent:healthcare:us-east:001", 4, 0.96)
    risk_routine = calculate_risk_score("PUBLIC", "READ", False)
    tier_routine = determine_triage_tier(passport_routine, risk_routine)
    passport_routine["governance"]["triage_rule"] = tier_routine
    token_routine = sign_passport(passport_routine)
    print(f"Scenario 1: Telemetry Data -> Tier: {tier_routine}")
    
    # Scenario 2: PHI access (ZK_PROOF)
    passport_zk = create_digital_passport("urn:agent:healthcare:us-east:002", 4, 0.87)
    risk_zk = calculate_risk_score("PHI", "READ", False)
    tier_zk = determine_triage_tier(passport_zk, risk_zk)
    passport_zk["governance"]["triage_rule"] = tier_zk
    print(f"Scenario 2: Patient Eligibility -> Tier: {tier_zk}")
    
    # Scenario 3: BFT (High-Risk)
    passport_bft = create_digital_passport("urn:agent:finance:eu-west:001", 5, 0.98)
    risk_bft = calculate_risk_score("PII", "UPDATE", True)
    tier_bft = determine_triage_tier(passport_bft, risk_bft)
    passport_bft["governance"]["triage_rule"] = tier_bft
    print(f"Scenario 3: Cross-Border Federation -> Tier: {tier_bft}")


if __name__ == "__main__":
    demonstrate_83_16_1_triage()
