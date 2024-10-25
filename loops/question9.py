def pair_with_target_sum(nums, target):
    seen_numbers = set()
    for num in nums:
        complement = target - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

numbers = [10, 20, 30, 40]
target_sum = 50
print(pair_with_target_sum(numbers, target_sum))  # Output: True
