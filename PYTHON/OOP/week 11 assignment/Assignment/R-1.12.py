"""                                 R-1.12 Solution

                  Q: Implement your own choice(data) function using only randrange. """
import random

def my_choice(data):
    n = len(data)                     # 1. find length
    rand_index = random.randrange(n)  # 2. pick random index 0 to n-1
    return data[rand_index]           # 3. return element at that index

items = ["apple", "banana", "cherry", "mango"]
print(my_choice(items))



# Pythonic Short Way
import random
my_choice = lambda data: data[random.randrange(len(data))]

items = [10, 20, 30, 40]
print(my_choice(items))
