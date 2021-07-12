# The list we will be iterating over.
numbers = [1, 2, 3, 4, 5]

# Function that will be called in the loop
def multiply(amount):
    return amount * 10

# The loop is wrapped in square brackets, and that list is returned to the variable
# called 'results'.
results = [multiply(value) for value in numbers]
# This will contain a new list, where each value in the old list will be multiplied by 10.
print(results)
