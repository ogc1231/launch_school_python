def union(list1, list2) :
    set1 = set(list1)
    set2 = set(list2)

    result = set1.union(set2)
    
    return result

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True