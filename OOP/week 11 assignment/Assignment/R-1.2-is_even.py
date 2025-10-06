"""    R-12    """
class even:
    def __init__(self, even):
        self._even = even
def is_even(k):
    # Agar number ko 2 se divide karne par remainder 0 aaye to even hai
    if k % 2 == 0:
        return True
    else:
        return False

# Test
print(is_even(4))   # True
print(is_even(7))   # False
