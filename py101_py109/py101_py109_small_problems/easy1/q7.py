def short_long_short(str1, str2):
    shorter = ""
    longer = ""

    if len(str1) < len(str2):
        shorter = str1
        longer = str2
    elif len(str1) > len(str2):
        shorter = str2
        longer = str1

    return shorter + longer + shorter

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")