def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0: # to see if divisor equally divides into number ot not
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(1))
print(factors(10))
print(factors(0))
print(factors(-1))
print(factors(-10))