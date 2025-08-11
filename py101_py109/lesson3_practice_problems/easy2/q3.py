# Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.

num1 = 42
num2 = 100
num3 = 101

print(num1 in range(10,100)) # True
print(num2 in range(10,100)) # False
print(num3 in range(10,100)) # False