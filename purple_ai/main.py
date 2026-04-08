from brain import AttackBrain
from recon import scan_target
from attacks import bruteforce, ddos, injection, phishing
from utils.logger import log
import random

brain = AttackBrain()

def execute_attack(name, target):
    if name == "bruteforce":
        return bruteforce.run(target)
    elif name == "ddos":
        return ddos.run(target)
    elif name == "injection":
        return injection.run(target)
    elif name == "phishing":
        return phishing.run(target)

def mutate_attack(base_attack):
    variants = {
        "injection": ["union-based", "boolean-based", "time-based"],
        "phishing": ["email", "sms", "voice"],
        "ddos": ["http-flood", "slowloris"],
        "bruteforce": ["dictionary", "credential stuffing"]
    }
    return random.choice(variants.get(base_attack, ["default"]))

def attack_chain(brain, target):
    print("\n🔥 Starting Multi-Step Attack Chain...\n")

    for step in range(3):
        attack = brain.choose_attack(target)
        variant = mutate_attack(attack)

        log(f"[STEP {step+1}] Attack: {attack} ({variant})")

        result = execute_attack(attack, target)
        log(f"Result: {result}")

        brain.update_learning(attack, result)

def main():
    log("🚀 Initializing Purple AI V2...")

    for round in range(5):
        print(f"\n⚡ ATTACK ROUND {round+1}")

        target = scan_target()
        log(f"Target Info: {target}")

        attack_chain(brain, target)

if __name__ == "__main__":
    main()
    