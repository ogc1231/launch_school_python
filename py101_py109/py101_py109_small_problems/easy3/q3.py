def print_in_box(str):
    line = f'+-{'-'*len(str)}-+'
    side = f'| {' '*len(str)} |'
    middle = f'| {str} |'

    print(line)
    print(side)
    print(middle)
    print(side)
    print(line)




print_in_box('To boldly go where no one has gone before.')
print_in_box('')