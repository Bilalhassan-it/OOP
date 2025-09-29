# p35.py
# Problem P-1.35: Birthday paradox simulation.

import random

class BirthdayParadox:
    def __init__(self, people):
        self.people = people

    def run_experiment(self, trials=1000):
        count = 0
        for _ in range(trials):
            birthdays = []
            for _ in range(self.people):
                bday = random.randint(1, 365)
                if bday in birthdays:
                    count += 1
                    break
                birthdays.append(bday)
        return count / trials
