import time

def run(target):
    print("[+] Simulating DDoS attack...")

    load = target["open_ports"]

    for i in range(load * 3):
        print(f"Request {i} sent")
        time.sleep(0.1)

    if target["security_level"] == "high":
        return "failed"
    elif target["security_level"] == "medium":
        return "partial"
    else:
        return "success"
    