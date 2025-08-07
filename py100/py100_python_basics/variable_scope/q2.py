x = 10

def my_function():
    x = x + 5
    print(x)

my_function() # UnboundLocalError, no arguemnt passed as parameter, x is shadowed with function but x is not intialised to a num