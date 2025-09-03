def after_midnight(time) :
    time_list = time.split(':')

    for i in range(len(time_list)):
        time_list[i] = int(time_list[i])
    
    sum = (time_list[0] * 60) + time_list[1]

    if sum == 1440 :
        sum = 0

    return sum

def before_midnight(time) :
    time_list = time.split(':')

    for i in range(len(time_list)):
        time_list[i] = int(time_list[i])
    
    sum = 1440 - ((time_list[0] * 60) + time_list[1])

    if sum == 1440 :
        sum = 0

    return sum



print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True