def reverse_number(num) :
    str_num = str(num)
    reversed_str_num = str_num[::-1]
    
    return int(reversed_str_num)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True