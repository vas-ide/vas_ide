from typing import Iterable


def replace_biggest(data: list[int]) -> Iterable[int]:
    lst_upd = []
    for number, item in enumerate(data):
        if number == len(data) - 1:
            lst_upd.append(-1)
        else:
            lst_upd.append(max(data[number + 1:]))
    return lst_upd


assert list(replace_biggest([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
assert list(replace_biggest([1, 2, 3, 4, 5, 6])) == [6, 6, 6, 6, 6, -1]
assert list(replace_biggest([1, 1, 1])) == [1, 1, -1]




