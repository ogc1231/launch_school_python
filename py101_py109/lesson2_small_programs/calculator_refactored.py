def print_msg(message):
    print(f'==> {message}')

def prompt(message):
    return input(f'==> {message}')

def invalid_number(num):
    try:
        int(num)
    except ValueError:
        return True
    return False

print_msg('Welcome to the calculator')

num1 = prompt("Enter first number: ")

while invalid_number(num1):
    print_msg('Not valid number')
    num1 = prompt("Enter first number: ")

num2 = prompt("Enter second number: ")

while invalid_number(num2):
    print_msg('Not valid number')
    num2 = prompt("Enter second number: ")

operation = prompt("""Enter operation:
                    1) add, 2) subtract, 3) multiply, 4) divide: """)

while operation not in ['1', '2', '3', '4']:
    print_msg('Not valid operation')
    operation = prompt("""Enter operation:
                        1) add, 2) subtract, 3) multiply, 4) divide: """)

match operation:
    case '1': # add
        result = int(num1) + int(num2)
    case '2': # subtract
        result = int(num1) - int(num2)
    case '3': # multiply
        result = int(num1) * int(num2)
    case '4': # divide
        result = int(num1) / int(num2)

print_msg(f'Result is: {result}')