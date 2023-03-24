



def div_con(x):
    sum_int = 0
    sum_str = 0
    for _ in x:
        if type(_) == str:
            sum_str += int(_)
        else:
            sum_int += _
    print(sum_int - sum_str)
    return sum_int - sum_str



















div_con([9, 3, '7', '3'])                                   #2
div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7])                  #14
div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0'])             #13
div_con(['1', '5', '8', 8, 9, 9, 2, '3'])                   #11
div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])               #61






