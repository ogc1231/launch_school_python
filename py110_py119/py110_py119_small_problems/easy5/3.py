def remove_vowels(string_list) :
    new_list = []
    

    for string in string_list :
        new_string = ''
        for char in string :
            if char  not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
                new_string += char
        new_list.append(new_string)

    return new_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True