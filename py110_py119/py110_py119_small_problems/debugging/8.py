import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original) # need yo use deepcopt not copy

original[0][0] = 99

print(copied[0] == [1])