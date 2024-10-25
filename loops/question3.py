def list_sum(numbers):
    total = 0
    for no in numbers:
        total += no
    return total


numbers = [1, 2, 3, 4, 5]
print("Sum of the list:", list_sum(numbers))
