




from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    lst_result = []
    for _, __ in enumerate(els):
        if len(lst_result) < 2:
            lst_result.append(__)
        else:
            if len(lst_result) < len(els):
                lst_result.append(sorted(els[_ - 2: _ + 1])[1])

    print(lst_result)
    return lst_result


median_three([1, 2, 3, 4, 5, 6, 7])                 #[1, 2, 2, 3, 4, 5, 6]
median_three([1])                                   #[1]

















