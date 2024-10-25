def reverse_list(strings):
    reversed_list = [s[::-1] for s in strings]
    return reversed_list

fruits = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_list(fruits))
