# change_maker.py
# Simple ChangeMaker class (Beginner Friendly)

class ChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)
        self.change = {}

    def make_change(self, charged, given): #(bill ki amount, yani saman ki price)
        if given < charged:                #(customer ne kitne paise diye)
            print("Not enough money given!")
            return

        amount = given - charged
        print(f"\nTotal change: {amount}")

        for d in self.denominations:
            count = amount // d   # how many notes/coins of this denomination
            if count > 0:
                self.change[d] = count
                amount -= d * count

    def show_change(self):
        print("\nChange breakdown:")
        for denom, count in self.change.items():
            print(f"{denom} : {count}")

"""..................................................................................................."""
# def make_change(amount_charged, amount_given):
#     """
#     Computes the change to give back using US denominations with the fewest bills and coins.
#     Returns a dictionary mapping denomination names to counts.
#     """
#     # US currency denominations (dollars and cents)
#     denominations = [
#         ("$100 bill", 10000),
#         ("$50 bill", 5000),
#         ("$20 bill", 2000),
#         ("$10 bill", 1000),
#         ("$5 bill", 500),
#         ("$1 bill", 100),
#         ("Quarter", 25),
#         ("Dime", 10),
#         ("Nickel", 5),
#         ("Penny", 1)
#     ]
    
#     # Convert dollars to cents to avoid floating point issues
#     change_cents = round((amount_given - amount_charged) * 100)
    
#     if change_cents < 0:
#         return "Insufficient amount given."
#     elif change_cents == 0:
#         return "No change required."
    
#     change = {}
#     for name, value in denominations:
#         count = change_cents // value
#         if count:
#             change[name] = count
#             change_cents -= count * value
#     return change