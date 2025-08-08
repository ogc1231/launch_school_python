length_m = int(input('enter the length of room: '))
width_m = int(input('enter the width of room: '))

area_m = length_m * width_m

area_f = area_m * 10.7639

print(f'{area_m} metres squared is {area_f:.2f} feet squared')