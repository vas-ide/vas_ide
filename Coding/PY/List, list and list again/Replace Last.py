from typing import Iterable


def replace_last(line: list) -> Iterable:
    lst_upd = []
    if len(line) > 0:
        lst_upd = [line[-1]]
        [lst_upd.append(item) for item in line]
        lst_upd = lst_upd[0:-1]
    return lst_upd

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []




