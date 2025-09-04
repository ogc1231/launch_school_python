def palindromes(string) :
    new_list = []
    result_list = []

    for i in range(len(string)) :
        for j in range(i + 1, len(string) + 1) :
            new_list.append(string[i:j])

    for sub in  new_list :
        if sub == sub[::-1] and len(sub) > 1 :
            result_list.append(sub)

    return result_list

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True