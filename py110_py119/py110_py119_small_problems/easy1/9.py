def string_to_signed_integer(string) :
    result = 0

    for char in string :
        if char.isalnum() :
            digit = ord(char) - ord('0')
            result = result * 10 + digit

    if string[0] == '-' :
        result *= -1
    elif string[0] == '+' :
        result *= 1

    return result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True