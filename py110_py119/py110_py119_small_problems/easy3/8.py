def sequence(count, start_num) :
    new_list = []

    for num in range(1, count + 1) :
        new_list.append(num * start_num)

    print(new_list)
    return new_list


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True