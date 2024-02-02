from typing import Iterable


def expand_intervals(items: Iterable) -> Iterable:
    lst_upd = []
    for item in items:
        if len(item) > 0:
            counter = item[0]
            while counter <= item[1]:
                lst_upd.append(counter)
                counter += 1
    return lst_upd


assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
assert list(expand_intervals([])) == []
assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]









