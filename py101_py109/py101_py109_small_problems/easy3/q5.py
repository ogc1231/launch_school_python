def triangle(num):
    for i in range(1, num + 1):
        spaces = num - i
        stars = i

        print(f'{' '*spaces}{'*'*stars}')


triangle(5)
triangle(9)