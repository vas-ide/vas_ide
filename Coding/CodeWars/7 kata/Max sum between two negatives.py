




def max_sum_between_two_negatives(arr):
    lst_res = []
    mark = 0
    arg_sum = 0
    for i in arr:
        if mark == 1 and i > 0:
            arg_sum += i
        elif mark == 0 and i < 0:
            mark = 1
        elif mark == 1 and i < 0:
            lst_res.append(arg_sum)
            arg_sum = 0
    lst_res.append(-1)
    print(f"{max(lst_res)}")
    return max(lst_res)

max_sum_between_two_negatives([-1, 6, -2, 3, 5, -7])            # 8
max_sum_between_two_negatives([5, -1, -2])                      # 0
max_sum_between_two_negatives([1, 6, -2, 3, 5, 7])              # -1




















