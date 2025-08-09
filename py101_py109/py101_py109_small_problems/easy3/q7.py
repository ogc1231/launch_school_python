
def twice(num):
    num_str = str(num)
    if len(num_str) % 2 == 0:
        first = num_str[0:len(num_str) // 2]
        last = num_str[len(num_str) // 2:]
        if first == last:
            return num
        else:
            return num*2
    else:
        return num*2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True