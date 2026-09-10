# p33.py
# Problem P-1.33: Handheld calculator with memory (inheritance).

from p33 import SimpleCalculator

class HandheldCalculator(SimpleCalculator):
    def __init__(self):
        self.memory = []

    def calculate_and_store(self, expression):
        result = super().calculate(expression)  # use parent method
        self.memory.append((expression, result))
        return result

    def show_memory(self):
        for exp, res in self.memory:
            print(f"{exp} = {res}")
