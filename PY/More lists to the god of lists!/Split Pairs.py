




from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    string = text
    if len(string) % 2 != 0:
        string += f"_"
    result_lst = []
    for _, __ in enumerate(string):
        if _ % 2 != 0:
            result_lst.append(f"{string[_-1: _+1]}")

    print(result_lst)
    return result_lst



split_pairs("abcd")                         #["ab", "cd"]
split_pairs("abc")                          #["ab", "c_"]
split_pairs("abcdf")                        #["ab", "cd", "f_"]
split_pairs("a")                            #["a_"]
split_pairs("")                             #[]


















