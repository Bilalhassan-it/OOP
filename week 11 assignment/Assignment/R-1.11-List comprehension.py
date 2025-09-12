"""   R-1.11: List comprehension practice   """

# Make list [1, 2, 4, 8, 16, 32, ... 256]

class List:
    def __init__(self, list):
        self._list = list
""" range(9) ka matlab hai 0,1,2,3,4,5,6,7,8.
Jab i = 0 hota hai: 2**0 = 1.
Isliye list ka pehla element 1 aata hai, na ke 0 """

powers = [0] + [2**i for i in range(9)]  #range(9) ka matlab hai 0,1,2,3,4,5,6,7,8.
print(powers)   


#total = 1
# for i in range(2*i in list[9]):
#      print(i)

