def is_even(k):
    """Return True if k is even, without using *, /, or % operators."""
    return (k & 1) == 0  # Last bit 0 → even, 1 → odd
# print(is_even(4))
# print(is_even(8))
# print(is_even(9))
# print(is_even(13))

#  User input
# if __name__ == "__main__":
#     try:
#         k = int(input("Enter an integer: "))
#         if is_even(k):
#             print(f"{k} is Even ✅")
#         else:
#             print(f"{k} is Odd ❌")
#     except ValueError:
#         print("Please enter a valid integer!")

