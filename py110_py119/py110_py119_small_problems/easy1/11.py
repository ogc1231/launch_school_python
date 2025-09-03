def signed_integer_to_string(num) :
    if num == 0 :
        return '0'
    
    result = ''

    if num < 0 :
        sign = '-'
    else :
        sign = '+'

    num = abs(num)

    while num > 0 :
        digit = num % 10
        char = chr(ord('0') + digit)
        result = char + result
        num = num //  10

    result = sign + result
    return result

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True