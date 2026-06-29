# ai-governance-guardrail
ai-governance-guardrail
# Enterprise AI Governance Guardrail & Audit Gateway

## Project Overview
An end-to-end automated governance gateway designed to intercept user prompts before they reach Large Language Models (LLMs). This project implements proactive risk mitigation controls aligned with **NIST AI RMF** and **ISO 42001** standards to ensure enterprise data privacy and policy compliance.

## Features Implemented
* **Automated Data Privacy Layer:** Scans and programmatically redacts PII (Emails, Phone Numbers) using pattern-matching arrays to prevent downstream data leakage.
* **Proactive Content & Risk Moderation:** Evaluates prompt intent against a corporate risk directory to immediately block prohibited queries (e.g., policy workarounds, security bypasses).
* **Compliance Audit Logging:** Generates structured, time-stamped audit trails tracking prompt classifications, actions taken (Passed, Sanitized, Blocked), and rule triggers.

## How It Works
The script evaluates user requests sequentially:
1. **Risk Evaluation:** Blocks execution if policy infractions are triggered.
2. **Sanitization:** Cleans sensitive data elements while keeping context.
3. **Execution Delivery:** Forwards only compliant, risk-vetted prompts to the target AI model.

---
© 2026 Sumeet Vasudev Saraf. All Rights Reserved.
