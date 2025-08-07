def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identify all of the identifiers

# line1 - multiply, left, right
# line2 - left, right

# line4 - get_num, prompt
# line5 - float, input, prompt

# line7 - first_number, get_num
# line8 - second_number, get_num
# line9 - product, multiply, first_number, second_number
# line10 - print, first_number, second_number, product