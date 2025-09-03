def string_to_integer(string) :
    result = 0

    for char in string :
        digit = ord(char) - ord('0')
        result = result * 10 + digit

    print(result)
    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True