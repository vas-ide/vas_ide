def nearest_value(values: set[int], one: int) -> int:
    # return min(values, key=lambda x: abs(x - one))

    if one in values:
        return one
    if len(values) == 1:
        return min(values)
    min_lst = [item for item in values if item < one]
    max_lst = [item for item in values if item > one]
    if len(min_lst) < 1:
        return min(max_lst)
    if len(max_lst) < 1:
        return max(min_lst)
    lst_upd = [max([item for item in values if item < one]), min([item for item in values if item > one])]
    if one - min(lst_upd) > max(lst_upd) - one:
        return max(lst_upd)
    return min(lst_upd)


assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5
