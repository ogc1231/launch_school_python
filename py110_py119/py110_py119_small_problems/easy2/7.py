def multiply_list(list1, list2) :
    new_list = []

    for num in range(len(list1)) :
        product = list1[num] * list2[num]
        new_list.append(product)

    return new_list


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True