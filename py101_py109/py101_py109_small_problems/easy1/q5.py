bill = int(input('What is the bill? '))
tip_percentage = int(input('What is the tip percentage? ')) / 100

tip = bill * tip_percentage
total = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')