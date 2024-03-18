import math


def int_palindrome(number: int, B: int) -> bool:

    # digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    # if base > len(digits): return None
    # result = ''
    # while number > 0:
    #     result = digits[number % base] + result
    #     number //= base
    # return result.upper() if upper else result
    #



    # mark = 0
    # if B == 2:
    #     inf = bin(number)[2:]
    #     if inf == inf[::-1]:
    #         mark = 1
    # if mark == 1:
    #     # print(True)
    #     return True
    # else:
    #     # print(False)
    #     return False
    # match B:
    #     case str(B) as system:
    #         pass
    #     case _:
    #         print(f"Неправильный  формат данных !")
    pass


int_palindrome(6, 2)
# == False
int_palindrome(34, 2)
# == False
int_palindrome(455, 2)
# == True
int_palindrome(20, 3)


# assert int_palindrome(6, 2) == False
# assert int_palindrome(34, 2) == False
# assert int_palindrome(455, 2) == True
