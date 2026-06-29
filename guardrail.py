import re
import datetime

class AIGovernanceGateway:
    def __init__(self):
        # Policy Control 1: Banned topics (Corporate Risk Management)
        self.banned_topics = ["corporate espionage", "insider trading", "bypass security"]
        
        # Policy Control 2: PII Detection Regex (Data Privacy Auditing)
        self.email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.phone_regex = r'\b\d{4}[-\s]?\d{3}[-\s]?\d{3}\b|\b\d{10}\b' # Matches standard 10-digit/Aus formats

    def log_audit_trail(self, status, message):
        """Generates a tamper-evident style compliance log entry."""
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] [AUDIT LOG] Status: {status} | Details: {message}")

    def enforce_input_policy(self, user_prompt: str) -> str:
        """Evaluates inbound prompts against enterprise risk policies."""
        # 1. Check for banned topics / policy violations
        for topic in self.banned_topics:
            if topic in user_prompt.lower():
                self.log_audit_trail("BLOCKED", f"Prompt violated safety policy. Detected topic: '{topic}'")
                raise ValueError("Access Denied: Prompt violates Enterprise AI Safety Policies.")

        # 2. Audit and Redact PII to prevent data leakage to external LLMs
        sanitized_prompt = user_prompt
        if re.search(self.email_regex, sanitized_prompt):
            sanitized_prompt = re.sub(self.email_regex, "[REDACTED_EMAIL]", sanitized_prompt)
        if re.search(self.phone_regex, sanitized_prompt):
            sanitized_prompt = re.sub(self.phone_regex, "[REDACTED_PHONE]", sanitized_prompt)

        if sanitized_prompt != user_prompt:
            self.log_audit_trail("SANITIZED", "PII was detected and programmatically redacted.")
        else:
            self.log_audit_trail("PASSED", "Prompt cleared initial privacy controls.")
            
        return sanitized_prompt

# =====================================================================
# SIMULATION / PROOF OF WORK
# =====================================================================
if __name__ == "__main__":
    gateway = AIGovernanceGateway()
    
    print("--- SIMULATION 1: Safe Enterprise Request ---")
    prompt_1 = "Can you draft a summary of our public Q1 marketing performance?"
    clean_prompt_1 = gateway.enforce_input_policy(prompt_1)
    print(f"Sent to LLM: {clean_prompt_1}\n")

    print("--- SIMULATION 2: PII Leakage Prevention Control ---")
    prompt_2 = "Please review this contract for john.doe@company.com or call me at 0412345678."
    clean_prompt_2 = gateway.enforce_input_policy(prompt_2)
    print(f"Sent to LLM: {clean_prompt_2}\n")

    print("--- SIMULATION 3: Policy Violation / Prohibited Content ---")
    prompt_3 = "How can I execute some corporate espionage without getting caught?"
    try:
        gateway.enforce_input_policy(prompt_3)
    except ValueError as e:
        print(f"Gateway Response: {e}\n")
