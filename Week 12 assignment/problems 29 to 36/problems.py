# problems.py
# Beginner-Friendly OOP solutions for P-1.29 → P-1.36

import random
import math

# ---------------- Problem P-1.29 ----------------
class PermutationGenerator:
    """Generate all possible strings of length n from given characters."""

    def __init__(self, characters):
        self.characters = characters

    def generate_strings(self, n, prefix=""):
        if n == 0:
            print(prefix)
        else:
            for ch in self.characters:
                self.generate_strings(n - 1, prefix + ch)


# ---------------- Problem P-1.30 ----------------
class DivisionCounter:
    """Count how many times an integer can be divided by 2 until it is < 2."""

    def __init__(self, number):
        self.number = number

    def count_divisions(self):
        count = 0
        n = self.number
        while n >= 2:
            n //= 2
            count += 1
        return count


# ---------------- Problem P-1.31 ----------------
class ChangeMaker:
    """Make change using minimum number of coins/bills."""

    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def make_change(self, charged, given):
        change = given - charged
        result = {}
        for d in self.denominations:
            if change >= d:
                result[d] = change // d
                change = change % d
        return result


# ---------------- Problem P-1.32 ----------------
class SimpleCalculator:
    """A simple calculator for +, -, *, /"""

    def calculate(self, expression):
        try:
            result = eval(expression)   # beginner level
            return result
        except Exception:
            return "Invalid expression"


# ---------------- Problem P-1.33 ----------------
class HandheldCalculator(SimpleCalculator):
    """Inherit from SimpleCalculator but keep memory of calculations."""

    def __init__(self):
        self.memory = []

    def calculate_and_store(self, expression):
        result = super().calculate(expression)  # use parent class method
        self.memory.append((expression, result))
        return result

    def show_memory(self):
        for exp, res in self.memory:
            print(f"{exp} = {res}")


# ---------------- Problem P-1.34 ----------------
class SentenceWriter:
    """Write a sentence multiple times."""

    def write_sentence(self, sentence, times=100):
        for i in range(times):
            print(f"{i+1}: {sentence}")


# ---------------- Problem P-1.35 ----------------
class BirthdayParadox:
    """Simulate birthday paradox probability."""

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


# ---------------- Problem P-1.36 ----------------
class WordCounter:
    """Count frequency of words in a text."""

    def __init__(self, text):
        self.text = text
        self.word_count = {}

    def count_words(self):
        words = self.text.split()
        for w in words:
            self.word_count[w] = self.word_count.get(w, 0) + 1

    def show_result(self):
        for w, c in self.word_count.items():
            print(w, ":", c)
