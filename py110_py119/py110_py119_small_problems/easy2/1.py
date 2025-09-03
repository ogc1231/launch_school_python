def dms(num) :
    degrees = int(num)
    minutes = int(num % 1 * 60)
    seconds = int((num % 1 * 60) % 1 * 60)

    result = f'{degrees}\u00B0{minutes:02d}\'{seconds:02d}\"'
    
    return result

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

