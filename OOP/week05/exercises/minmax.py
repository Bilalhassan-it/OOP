def minmax(data):
    """ takes a sequence of one or more numbers, and returns the smallest and largest numbers,"""
    smallest = data[0]
    largest = data[0]

    for value in data[1]:
        if value < smallest:
            smallest = value
            if value > largest:
                largest = value
                return (smallest, largest)
            
            numbers = [8, 4, 6, 1, 10]
result = minmax("numbers")
print(result)  # Output: (1, 9)

        
# if __name__ == "__main__":
#     try:
#         n = int(input("Enter an integer: "))
#         if is_even(k):
#             print(f"{n} is Even ✅")
#         else:
#             print(f"{n} is Odd ❌")
#     except ValueError:
#         print("Please enter a valid integer!")
        