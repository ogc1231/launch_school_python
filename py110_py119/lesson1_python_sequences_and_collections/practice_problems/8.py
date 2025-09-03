statement = "The Flintstones Rock"

statement_list = list(statement)

new_dict = {}

for char in statement_list :

    if char.isalpha() :
        new_dict[char] = new_dict.get(char, 0) + 1

print(new_dict)