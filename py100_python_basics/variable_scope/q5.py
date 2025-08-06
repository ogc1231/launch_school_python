a = 1

def my_function():
    print(a)
    a = 2

my_function() # UnboundLocalError, a wihtin function shadows a in global scope but is decalres after print so is unreachcbale