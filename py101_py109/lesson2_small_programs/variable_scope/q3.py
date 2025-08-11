num = 5

def my_func():
    global num # makes variables inside function available in global scope
    num = 10

my_func() # nothing, does not print or return anything
print(num) # 10, num resigned to 10 inside function, global num makes it available in global scope