title = "Flintstone Family Members"

spaces_total = 40

spaces_minus_title = spaces_total - len(title)

spaces_left = spaces_minus_title // 2
spaces_right = spaces_minus_title - spaces_left

print(f'{' '*spaces_left}{title}{' '*spaces_right}')
print(title.center(40))

