def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x) # Inner 1: 25

    def inner_func2():
        print("Inner 2:", x) # Inner 2: 15, 15 is in outerscope

    inner_func1()
    inner_func2()

my_func() 