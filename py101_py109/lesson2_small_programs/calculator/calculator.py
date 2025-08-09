# ask user for first number
# ask user for second number
# ask user for operation
# perform operation
# ouput result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation: 1) add, 2) subtract, 3) multiply, 4) divide: ")
result = 0

if operation == '1':
    result = num1 + num2
elif operation == '2':
    result = num1 - num2
elif operation == '3':
    result = num1 * num2
elif operation == '4':
    result = num1 / num2

print(f'Result is {result}')