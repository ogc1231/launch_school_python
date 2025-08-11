def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer() # prints Hello World, outer is invoked, outer_var intialised to "hello", inner invoked, inner_var intialised as World botth values printed