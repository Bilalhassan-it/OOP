# p30.py
# Problem P-1.30: Count how many times an integer can be divided by 2 until < 2.

class DivisionCounter:
    def __init__(self, number):
        self.number = number

    def count_divisions(self):
        count = 0
        n = self.number
        while n >= 2:
            n //= 2
            count += 1
        return count
