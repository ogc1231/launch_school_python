def multiply_items(list1, list2) :
    new_list = []

    for num in range(len(list1)) :
        new_list.append(list1[num] * list2[num])

    return new_list

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True