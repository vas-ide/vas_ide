def remove_min_max(data: set[int], total: int) -> set[int]:
    for i in range(total):
        if len(data) > 0:
            data.remove(min(data))
        if len(data) > 0:
            data.remove(max(data))
    return data




assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()
