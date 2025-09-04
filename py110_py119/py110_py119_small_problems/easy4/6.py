def leading_substrings(string) :
    new_list = []
    result = ''

    for char in string :
        result += char
        new_list.append(result)

    return new_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])