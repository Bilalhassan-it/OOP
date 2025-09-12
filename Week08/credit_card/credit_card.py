# credit_card.py

class CreditCard:
    """ A consumer credit card example """

    def __init__(self, customer, bank, account, limit):
        """Customer, bank, account, and limit initialize करते हैं"""
        self._customer = customer   # customer ka naam
        self._bank = bank           #bank ka name 
        self._account = account     #account number 
        self._limit = limit         #max limit
        self._balance = 0  # starting balance is zero

    # --- Getter methods ---
    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    # --- Main Methods ---
    def charge(self, price):
        """agar price + balance > limit ho jaye to transaction reject hoga"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """payment karne par balance kam ho jayega"""
        self._balance -= amount
