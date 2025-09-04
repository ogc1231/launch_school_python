def keep_keys(input_dict, keys) :
    new_dict = {}

    for key in input_dict :
        if key in keys :
            new_dict[key] = input_dict[key]

    return new_dict

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True