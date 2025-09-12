"""    R-13   """
def minmax(data):
    smallest = data[0]
    largest = data[0]

    for val in data:
        if val < smallest:
            smallest = val
        elif val > largest:
            largest = val
    
    return (smallest, largest)

# Test
print(minmax([3, 5, 1, 8, -2, 7]))   # (-2, 8)
