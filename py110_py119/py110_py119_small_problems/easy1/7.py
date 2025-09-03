def swap(string) :
    if len(string) <= 1 :
        return string
    
    string_list = string.split(' ')
    new_list = []

    for word in string_list :
        if len(word) > 1 :
            new_word = word[-1] + word[1:-1] + word[0]
            new_list.append(new_word)
        else :
            new_list.append(word)
    
    new_string = ' '.join(new_list)
    return new_string

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True