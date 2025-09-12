"""    R-14    """
def sum_of_squares(n): #sum of SQ mean 25*5=25 h iska iska 5 jis k sath y Mul howa h wo bhi add hoga 25+5=30
    total = 0
    for i in range(1, n):  #i jo h wo like 1 2 3 4 5 tk k number ly ga i loop h 1 sy 4 tk 
        total += i*i  #5+=5*5=30
    return total

"""   R-15 invovlved  """
# Pythonic way
def sum_of_squares_py(n):
     return sum([i*i for i in range(1, n)])

# R-14 Test
print(sum_of_squares(5))     # 1^2 + 2^2 + 3^2 + 4^2 = 30
#R-15 test
print(sum_of_squares_py(5))  # 30
