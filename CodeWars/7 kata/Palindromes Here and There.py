




def convert_palindromes(numbers):
    lst = []
    for _ in numbers:
        if f"{_}" == str(_)[::-1]:
            lst.append(1)
        else:
            lst.append(0)
    print(lst)
    return lst


convert_palindromes([101, 2, 85, 33, 14014])                        #[1, 1, 0, 1, 0]
convert_palindromes([45, 21, 303, 56])                              #[0, 0, 1, 0]














