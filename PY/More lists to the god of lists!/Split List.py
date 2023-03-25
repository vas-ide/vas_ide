




from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    result_lst = [[], []]
    for _, __ in enumerate(items):
        if _ < len(items) / 2:
            result_lst[0].append(__)
        else:
            result_lst[1].append(__)
    print(result_lst)
    return result_lst


split_list([1, 2, 3, 4, 5, 6])                                              #[[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3])                                                       #[[1, 2], [3]]
split_list(["banana", "apple", "orange", "cherry", "watermelon"])           #[["banana", "apple", "orange"], ["cherry", "watermelon"]]
split_list([1])                                                             #[[1], []]
split_list([])                                                              #[[], []]















