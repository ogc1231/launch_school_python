from datetime import datetime

current_year = datetime.now().year

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

time_left = retire_age - age
retire_year = current_year + time_left

print(f'It\'s {current_year}. You will retire in {retire_year}.')
print(f'You have only {time_left} years of work to go!')

