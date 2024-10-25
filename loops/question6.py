def find_max(numbers):
    max_num = numbers[0]  # Initialize with the first element
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

nums = (10, 20, 30, 40, 50)
print("Largest number:", find_max(nums))
