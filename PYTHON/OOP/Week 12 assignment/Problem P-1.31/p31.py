# p31.py
# Problem P-1.31: Make change using minimum coins/bills.

class ChangeMaker:
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
