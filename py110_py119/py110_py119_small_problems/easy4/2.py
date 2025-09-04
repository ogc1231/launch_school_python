def merge_sets(list1, list2) :
    new_set = set(list1).union(set(list2))
    return new_set

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True