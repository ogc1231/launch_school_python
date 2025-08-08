def xor(ele1, ele2):
    if (ele1 and not ele2) or (ele2 and not ele1):
        return True
    return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)