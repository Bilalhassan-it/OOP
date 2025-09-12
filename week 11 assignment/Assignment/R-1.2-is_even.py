"""    R-12    """
def is_even(k):
    # Agar number ko 2 se divide karne par remainder 0 aaye to even hai
    if k % 2 == 0:
        return True
    else:
        return False

# Test
print(is_even(4))   # True
print(is_even(7))   # False
