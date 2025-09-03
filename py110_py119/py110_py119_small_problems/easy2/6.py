def multiplicative_average(num_list) :
    total = 1
    num_elements = len(num_list)

    for num in num_list :
        total *= num

    result = total / num_elements
    final_result = f'{result:.3f}'
    
    return str(final_result)


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")