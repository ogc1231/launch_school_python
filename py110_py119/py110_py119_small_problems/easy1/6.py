def word_sizes(input) :
    input_list = input.split()
    new_input_list = []
    count = {}
    
    for word in input_list :
        new_word = ''
        for char in word :
            if char.isalpha() :
                new_word += char
        new_input_list.append(new_word)

    for word in new_input_list :
        size = len(word)
        count[size] = count.get(size, 0) + 1

    return count
    
# All of these examples should print True
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})