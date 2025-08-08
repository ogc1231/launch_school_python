def calculate_sum(num):
    sum = 0
    for i in range(1,num + 1):
        sum += i
    return sum

def calculate_product(num):
    product = 1
    for i in range(1,num + 1):
        product *= i 
    return product

num = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if operation == 's':
        print(f'The sum of the integers between 1 and {num} is {calculate_sum(num)}.')
elif operation == 'p':
        print(f'The product of the integers between 1 and {num} is {calculate_product(num)}.')
