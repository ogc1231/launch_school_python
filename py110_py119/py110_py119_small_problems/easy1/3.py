def is_real_palindrome(string) :
    new_string = ''

    for char in string :
        if char.isalnum() :
            new_string += char.casefold()
    
    if new_string == new_string[::-1] :
        return True
    
    return False


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True