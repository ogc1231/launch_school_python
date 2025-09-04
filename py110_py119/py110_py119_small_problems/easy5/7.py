def sum_digits(num) :
    num_string = str(num)
    sum = 0;

    for char in num_string :
        sum += int(char)

    return sum

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True