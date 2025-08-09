def century(year):
    century = 0
    if year % 100 == 0:
        century = (year // 100)
    else:
        century = (year // 100) + 1

    century_str = str(century)

    if len(century_str) > 1:
        if century_str[-2] == '1':
            return century_str + 'th'
        elif century_str[-1] == '1':
            return century_str + 'st'
        elif century_str[-1] == '2':
            return century_str + 'nd'
        elif century_str[-1] == '3':
            return century_str + 'rd'
        else:
            return century_str + 'th'
    elif century_str == '1':
        return century_str + 'st'
    elif century_str == '2':
        return century_str + 'nd'
    elif century_str == '3':
        return century_str + 'rd'
    else:
            return century_str + 'th'
    
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True