def is_empty_or_blank(str):
  if len(str.strip(' ')) == 0:
    return True
  else:
    return False

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True