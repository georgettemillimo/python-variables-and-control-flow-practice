def keys_greater_than_n(d, n):
    result = [key for key, value in d.items() if value > n]
    return result


sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print("Keys with values greater than", n, ":", keys_greater_than_n(sample_dict, n))
