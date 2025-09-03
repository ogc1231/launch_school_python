def integer_to_string(num) :
    if num == 0 :
        return '0'
    
    result = ''

    while num > 0 :
        digit = num % 10
        char = chr(ord('0') + digit)
        result = char + result
        num = num // 10

    return result



print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True