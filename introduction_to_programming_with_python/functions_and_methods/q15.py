def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# classify the identifiers as global, local, or built-in

# global - multiply, get_num, first_number, second_number, product
# local - left, right, prompt,
# built-in - print, input, float