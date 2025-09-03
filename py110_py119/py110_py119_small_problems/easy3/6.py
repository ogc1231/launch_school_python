def sequence(num) :
    new_list = []

    for num in  range(1, num + 1) :
        new_list.append(num)

    return new_list

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True