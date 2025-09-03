def double_consonants(sting) :
    new_string = ''

    for char in sting :
        if char.isalpha() and char not in ['a', 'e', 'i', 'o', 'u'] :
            new_string += (char * 2)
        else :
            new_string += char

    return new_string


# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")