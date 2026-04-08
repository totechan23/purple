import time

def run(target):
    print("[+] Starting Bruteforce Attack...")

    if not target["login"]:
        print("[-] No login system found")
        return "failed"

    for i in range(5):
        print(f"Trying password_{i}")
        time.sleep(0.3)

    if target["security_level"] == "high":
        return "failed"
    elif target["security_level"] == "medium":
        return "partial"
    else:
        return "success"
    