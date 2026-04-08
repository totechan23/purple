import random

class AttackBrain:
    def __init__(self):
        self.history = []
        self.success_score = {
            "bruteforce": 1,
            "ddos": 1,
            "injection": 1,
            "phishing": 1
        }

    def choose_attack(self, target_info):
        score = self.success_score.copy()

        if target_info.get("login"):
            score["bruteforce"] += 3

        if target_info.get("input_fields"):
            score["injection"] += 4

        if target_info.get("open_ports") > 3:
            score["ddos"] += 2

        if target_info.get("email_exposed"):
            score["phishing"] += 3

        attacks = list(score.keys())
        weights = list(score.values())

        return random.choices(attacks, weights=weights)[0]

    def update_learning(self, attack, result):
        if result == "success":
            self.success_score[attack] += 2
        elif result == "partial":
            self.success_score[attack] += 1
        else:
            self.success_score[attack] = max(1, self.success_score[attack] - 1)
            