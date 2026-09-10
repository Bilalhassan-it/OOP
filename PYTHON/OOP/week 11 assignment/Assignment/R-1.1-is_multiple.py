"""   R-11   """
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

# Example
print(is_multiple(15, 55))  # True
print(is_multiple(9, 5))   # False

