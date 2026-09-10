# main.py

from credit_card import CreditCard

if __name__ == "__main__":
    # ek khaali list banayi jisme hum cards rakhte hain
    wallet = []   #array or list

# append ka matlab hota hai list ke andar ek naya element dalna
    wallet.append(CreditCard('Bilal Hassan', 'Karachi Saving',  #append sirf ek list me naya element dalne ka tareeqa hai.
                             '5391 0375 9387 5309', 3000))
    wallet.append(CreditCard('Bilal Hassan', 'Multan Federal',
                             '3485 0399 3395 1954', 4000))
    wallet.append(CreditCard('Bilal Hassan', 'karachi Finance',
                             '5391 0375 9387 5309', 5000))

    # cards par charges lagana
    for val in range(1, 17):
        wallet[0].charge(val)         
        wallet[1].charge(2 * val)    
        wallet[2].charge(3 * val)     

    # har card ki detail print karna
    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()
