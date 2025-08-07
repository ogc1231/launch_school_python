def is_empty(str):
  if len(str) != 0:
    return False
  else:
    return True

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True