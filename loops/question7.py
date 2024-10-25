def remove_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


numbers = [1, 2, 2, 3, 4, 4, 5]
print("Here is the list without duplicates:", remove_duplicates(numbers))
