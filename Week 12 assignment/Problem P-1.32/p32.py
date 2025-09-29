# p32.py
# Problem P-1.32: Simple calculator.

class SimpleCalculator:
    def calculate(self, expression):
        try:
            result = eval(expression)   # only for learning (not secure in real apps)
            return result
        except Exception:
            return "Invalid expression"
