def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first()) # {'prop1': "hi there"}
print(second()) # None

# don't return same thing, if there's nothing after a return statement, the function will return None