def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# ln 5 to ln 11 define a dictionary
# ln 13 calls do_something function with my_dict passed in as the argument
# ln 1 to 2 defines the do_something fucntions
# ln 1 dictionary in the parameter
# ln 2 dictionary keys are selected and sorted, then the key at index 1 is chnaged to uppercase and the value returned
# ln 13 CHRIS is printed 