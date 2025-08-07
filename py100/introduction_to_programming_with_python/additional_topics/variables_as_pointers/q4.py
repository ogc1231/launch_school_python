dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a']) # [1, 42, 3]

# dict2 is makes a copy of dict1 (new object), but mutating dict1 with effect dict2
# dict creates a shallow copy
# both dict refernce the same list inside them