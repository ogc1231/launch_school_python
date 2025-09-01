nums = []

nums.append(input('Enter the 1st number: '))
nums.append(input('Enter the 2nd number: '))
nums.append(input('Enter the 3rd number: '))
nums.append(input('Enter the 4th number: '))
nums.append(input('Enter the 5th number: '))
num_last = input('Enter the last number: ')

num_list = ','.join(nums)

if (num_last in num_list):
    print(f'{num_last} is in {num_list}.')
else:
    print(f'{num_last} isn\'t in {num_list}.')
