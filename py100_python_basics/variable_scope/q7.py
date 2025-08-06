a = 1

def my_function():
    global a
    a = 2

my_function()
print(a) #2, global a is declared inside the function so insides the function is now global scope too