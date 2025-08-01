foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# prints 'bar, foo in global scope, set_foo doesn;t return an value