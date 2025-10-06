"""   R-1.6: Sum of squares of odd    """
def _Sum_of_squares_odd(n):
    total = 0

    for i in range(1, n):
        if i % 2 != 0:  #check odd :   agr even orint krwan hi to == ayga
          total += i*i
    return total

# Pythonic way R-1.7
def sum_of_squares_odd_py(n):
    return sum([i*i for i in range(1,n) if i % 2 != 0 ])

# Test
print(_Sum_of_squares_odd(6))   # 1^2 + 3^2 + 5^2 = 35

# Test R-1.7
print(sum_of_squares_odd_py(6)) # 35




