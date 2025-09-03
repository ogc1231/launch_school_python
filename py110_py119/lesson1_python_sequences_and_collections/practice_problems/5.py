ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# total = 0

# for person in ages :
#     age = ages[person]
#     total += age
# print(total) # 6174

total = sum(ages.values())
print(total) # 6174