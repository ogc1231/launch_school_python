def running_total(num_list) :
    new_list = []
    sum = 0

    for num in num_list :
        sum += num
        new_list.append(sum)
    
    return new_list



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True