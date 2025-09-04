def unique_sequence(list1) :
    new_list = []

    for num in list1 :
        if num not in new_list :
            new_list.append(num)

    return new_list


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True