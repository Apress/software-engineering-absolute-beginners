def sum(*numbers):
    total = 0  # initialise total to 0
    for number in numbers:
        total += number
    return (total)


print(sum(10, 56))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
