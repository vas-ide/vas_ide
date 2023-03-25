


import numpy as np


def list_beautify(data: list[list[int]]) -> str:
    print(np.array(data))
    # str_result = "["
    # for i in data:
    #     lst = []
    #     for j in i:
    #         lst.append(f'{j:>4}')
    #     str_result += f'{lst},\n '
    # str_result = str_result[:-3] + f"]"
    # print(str_result)
    # return str_result


    print(np.array(data))


list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
#"[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
# list_beautify([[1, 10, 100, -1000]])
# #"[[1, 10, 100, -1000]]"
# list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
# #"[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
# list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
# #"[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
#



























