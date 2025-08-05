# Assume that obj already has a value of 42
# Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? 

obj = 'ABcd' # reassign, obj = 'ABcd'
obj.upper() # neither,
obj = obj.lower() # reassign, obj = 'abcd'
print(len(obj)) # neither,
obj = list(obj) # reassign, obj = ['a', 'b', 'c', 'd']
obj.pop() # mutation, obj = ['a', 'b', 'c']
obj[2] = 'X' # mutation, obj = ['a', 'b', 'X']
obj.sort() # mutation, obj = ['X', 'a', 'b']
set(obj) # neither,
obj = tuple(obj) # reassign, obj = ('X', 'a', 'b')