# 1: a function that returns the sum of two numbers

# informal pseudocode
# create a function with two parameters, one for each number
# inside the body of the fuction return the value of the two numbers summed together
# invoke the function with two numbers passed in as arguments
# print out returned value

# formal pseudocode
# START
# a function that returns the sum of two numbers

# FUNCTION sum_numbers(num1, num2)
#   BEGIN
#       RETURN num1 + num2
#   END

# PRINT sum_numbers(1, 2)
# END

# 2: a function that takes a list of strings, and returns a string that is all those strings concatenated together 

# informal pseudocode
# create a variable result and intialise it as an empty string
# create a function which takes in a list of strings as a paramter
# iterate through all strings in the lists, concantenating them with result each iteration
# return result
# invoke function with list passed as an argument
# print out result

# formal pseudocode
# START
# result = ''

# FUNCTION join_strings(list_strings)
#   BEGIN
#       FOR i < len(list_strings)
#           result += list_strings[i]
#       RETURN result
#   END

# PRINT join_strings(list_strings)
# END

# 3: a function that takes a list of integers, and returns a new list with every other element from the original list, starting with
# the first element.

# informal
# create an empty list called result
# create a fuction which takes in a list of integers as a parameter
# in th body of the function loop thorugh the list append numbers at even index to results list
# return results list
# invoke function with list of integers passed in as the argument
# print the result