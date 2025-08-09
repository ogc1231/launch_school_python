def clean_up(string):
    result = ''
    prev_is_space = False

    for char in  string:
        if char.isalpha():
            result += char
            prev_is_space = False
        else:
            if not prev_is_space:
                result += ' '
                prev_is_space = True
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
