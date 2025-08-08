def is_odd(num):
    if abs(num) % 2 == 1:
        return True
    return False


print(is_odd(-1))
print(is_odd(1))
print(is_odd(-2))
print(is_odd(2))