def time_of_day(num) :
    minutes_in_day = 24 * 60

    num = num % minutes_in_day
   
    hour = num // 60
    minute = num % 60
    
    result = f'{hour:02d}:{minute:02d}'
    return result

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True