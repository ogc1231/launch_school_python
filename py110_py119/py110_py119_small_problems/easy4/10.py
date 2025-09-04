def is_item_available(num, transactions) :
    new_list = transactions_for(num, transactions)
    sum_list = []

    for transaction in new_list :
        if transaction['movement'] == 'in' :
            sum_list.append(transaction['quantity'])
        elif transaction['movement'] == 'out' :
            sum_list.append(transaction['quantity'] * -1)

    total = sum(sum_list)

    if total > 0 :
        return True
    else :
        return False

def transactions_for(num, transactions) :
    new_list = []

    for transaction in transactions :
        if transaction['id'] == num :
            new_list.append(transaction)

    return new_list

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True