def substrings(string) :
    new_list = []

    for i in range(len(string)) :
        for j in range(i + 1, len(string) + 1) :
            new_list.append(string[i:j])
    
    return new_list

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True