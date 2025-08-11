def is_color_valid(color):
    return color == "blue" or color == "green"


def is_color_valid2(color):
    return color in ['blue', 'green']


print(is_color_valid('green'))
print(is_color_valid('blue'))
print(is_color_valid('red'))

print(is_color_valid2('green'))
print(is_color_valid2('blue'))
print(is_color_valid2('red'))