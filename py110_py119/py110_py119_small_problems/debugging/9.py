data_set = {1, 2, 3, 4, 5}

for item in list(data_set):
    if item % 2 == 0:
        data_set.remove(item)

print(data_set)
# set is being muatated and the elements being shifted