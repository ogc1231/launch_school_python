nums = (1, 2, 3, 4, 5)
print(nums)

new_nums = list(nums)[1:4]

new_nums.reverse()
result = tuple(new_nums)
print(result)
