def is_balanced(string) :
    balance = 0

    for char in string :
        if char == '(' :
            balance += 1
        elif char == ')' :
            balance -= 1
        
        if balance < 0:
            return False
        
    return balance == 0
     


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True