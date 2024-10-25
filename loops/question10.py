def tuples_list_dict(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict

# Example usage
tuples = [("apple", 5), ("Mango", 3), ("Oramges", 7)]
print(tuples_list_dict(tuples))
