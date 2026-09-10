def sum_of_squares(n):
    """Return the sum of the squares of all positive integers less than n."""
    value = 0
    for i in range(0, n):
        value += i * i
    return value
print(sum_of_squares(5))


# ✅ Take user input
# try:
#     n = int(input("Enter a positive integer: "))
#     if n > 0:
#         print("Sum of squares of numbers less than", n, "is:", sum_of_squares(n))
#     else:
#         print("Please enter a positive integer!")
# except ValueError:
#     print("Invalid input! Please enter an integer.")



    