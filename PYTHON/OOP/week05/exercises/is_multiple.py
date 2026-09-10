def is_multiple(n, m):
    """Return True if n is a multiple of m, otherwise False."""
    if m == 0:  # Avoid division by zero
        return False
    return n % m == 0

# Example usage
print(is_multiple(10, 5))   # True  (10 is a multiple of 5)
print(is_multiple(12, 7))   # False (12 is not a multiple of 7)
print(is_multiple(0, 3))    # True  (0 is a multiple of any non-zero number)
print(is_multiple(5, 0))    # False (division by zero is invalid)

