numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

new_list = []

for num in numbers:
 new_list.append(numbers[num] // 2)

print(new_list)