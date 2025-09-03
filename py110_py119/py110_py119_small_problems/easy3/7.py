def swap_name(string) :
    string_list = string.split(' ')
    result =  f'{string_list[-1]}, {string_list[0]}'

    return result

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True