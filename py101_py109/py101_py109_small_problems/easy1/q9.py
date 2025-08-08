def is_leap_year(num):
    if num >= 1752:
        return is_leap_year_gregorian(num)
    else:
        return is_leap_year_julian(num)


def is_leap_year_gregorian(num):
    return (num % 400 == 0) or ((num % 4 == 0) and (num % 100 != 0))

def is_leap_year_julian(num):
    return num % 4 == 0

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)