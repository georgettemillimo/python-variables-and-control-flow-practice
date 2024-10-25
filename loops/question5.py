def print_even_keys(k):
    for key, value in k.items():
        if value % 2 == 0:
            print(key)

dictionary = {'a': 2, 'b': 3, 'c': 4}
print_even_keys(dictionary)
