import random

def scan_target():
    return {
        "open_ports": random.randint(1, 5),
        "login": random.choice([True, False]),
        "input_fields": random.choice([True, False]),
        "email_exposed": random.choice([True, False]),
        "security_level": random.choice(["low", "medium", "high"])
    }
