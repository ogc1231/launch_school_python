munsters_description = "The Munsters are creepy and spooky."

munsters_description_list = munsters_description.lower().split(' ')

word1 = munsters_description_list[0][0:1] + munsters_description_list[0][1:].upper()
word2 = munsters_description_list[1][0:1] + munsters_description_list[1][1:].upper()

result = f'{word1} {word2} {' '.join(munsters_description_list[2:])}' 

print(result)

munsters_description2 = "The Munsters are creepy and spooky."

print(munsters_description2.swapcase())