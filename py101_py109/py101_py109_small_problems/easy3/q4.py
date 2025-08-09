def stringy(num):
    str = '10'
    result = ''
    if num % 2 == 1:
        result = str*(num // 2) + '1'
    elif num % 2 == 0:
        result = str*(num // 2)
    return result




print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True