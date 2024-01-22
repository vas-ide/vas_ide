




from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    class Analiz:
        def __init__(self):
            self.lst_result = []

        def calc(self, arr):
            for _ in arr:
                if type(_) == list:
                    self.calc(_)
                else:
                    self.lst_result.append(_)

    result = Analiz()
    result.calc(array)
    print(result.lst_result)
    return result.lst_result









flat_list([1, 2, 3])                                #[1, 2, 3]
flat_list([1, [2, 2, 2], 4])                        #[1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])    #[2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1])                   #[-1, 1, -2, 1, -1]

















