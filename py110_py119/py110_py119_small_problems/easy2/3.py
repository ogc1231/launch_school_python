def halvsies(num_list) :
    result_list = []

    if len(num_list) % 2 == 0 :
        left_list = list(num_list[0:len(num_list) // 2])
        right_list = list(num_list[len(num_list) // 2:])
    else :
        left_list = list(num_list[0:len(num_list) // 2 + 1])
        right_list = list(num_list[len(num_list) // 2 + 1:])


    result_list.append(left_list)
    result_list.append(right_list)

    return result_list

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])