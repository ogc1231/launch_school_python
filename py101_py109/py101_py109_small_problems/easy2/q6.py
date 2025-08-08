def penultimate(str):
    str_list = str.split(' ')
    if len(str_list) > 0:
        return str_list[-2]
    else:
        return str

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")