def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# SyntaxError: parameter without a default follows parameter with a default, third needs a deafult value