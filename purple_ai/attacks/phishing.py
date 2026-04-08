import random

def run(target):
    print("[+] Launching phishing attack...")

    if not target["email_exposed"]:
        print("[-] No email target found")
        return "failed"

    templates = [
        "Your account is locked. Click to verify.",
        "Urgent: Reset your password now!",
        "Security alert: Suspicious login attempt detected."
    ]

    msg = random.choice(templates)
    print(f"Phishing Message: {msg}")

    if target["security_level"] == "high":
        return "failed"
    elif target["security_level"] == "medium":
        return "partial"
    else:
        return "success"
    