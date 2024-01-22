from typing import Iterable, Any


def remove_after_kth(items: list[Any], k: int) -> Iterable[Any]:
    if k == 0:
        return []
    dict_count = {}
    lst_upd = []
    for item in items:
        if item not in dict_count:
            dict_count[item] = 1
            lst_upd.append(item)
        else:
            dict_count[item] += 1
            if dict_count[item] <= k:
                lst_upd.append(item)
    return lst_upd

assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]
