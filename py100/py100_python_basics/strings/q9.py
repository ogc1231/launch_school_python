def starts_with(str1, str2):
  if str1.startswith(str2):
    return True
  else:
    False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True