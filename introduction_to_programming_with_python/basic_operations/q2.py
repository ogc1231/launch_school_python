num = 4936

last = num % 10
second_last = (num % 100) // 10
second = (num % 1000) // 100
first = num // 1000


print(last)
print(second_last)
print(second)
print(first)