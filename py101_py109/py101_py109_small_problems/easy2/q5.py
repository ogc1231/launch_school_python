num1 = float(input('==> Enter the first number: '))
num2 = float(input('==> Enter the second number: '))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
floor_quotient = num1 // num2
remainder = num1 % num2
power = num1**num2

print(f'{num1} + {num2} = {add}')
print(f'{num1} - {num2} = {subtract}')
print(f'{num1} * {num2} = {multiply}')
print(f'{num1} / {num2} = {divide}')
print(f'{num1} // {num2} = {floor_quotient}')
print(f'{num1} % {num2} = {remainder}')
print(f'{num1} ** {num2} = {power}')