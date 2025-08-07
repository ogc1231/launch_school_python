text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8, this returns a new string after the slice and then return the index
print(text.rfind('f', 21, 35))    # 29, searcg between 21 and 35 index and retuens index

