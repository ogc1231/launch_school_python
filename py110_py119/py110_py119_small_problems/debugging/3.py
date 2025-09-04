def multiply_list(lst):
    for i in range(len(lst)) :
        lst[i] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])