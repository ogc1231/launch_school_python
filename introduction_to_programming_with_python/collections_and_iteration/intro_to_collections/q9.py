my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)


# Are the lists assigned to my_list and another_list equal?
# the values are the same in both lists, True

# Are the lists assigned to my_list and another_list the same object?
# they are not the same object, False

# Are the nested lists at index 3 of my_list and another_list equal?
# the values are the same, True

# Are the nested lists at index 3 of my_list and another_list the same object?
# they are the same object, referencing the same object, lis constructor creates a shallow copy