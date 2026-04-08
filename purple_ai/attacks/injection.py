def run(target):
    print("[+] Attempting SQL Injection...")

    if not target["input_fields"]:
        print("[-] No input fields available")
        return "failed"

    if target["security_level"] == "high":
        print("WAF detected. Trying bypass...")
        return "partial"

    return "success"
