set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2) # {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# set1 and set2 refernce the same object in memory, so mutates one will effect the other
