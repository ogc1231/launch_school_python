def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

# the return value from decrease was being used as the reassignedment for counter