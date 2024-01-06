import numpy as np

def weak_point(matrix):
    np_arr = np.array(matrix)
    np_lst_x = np_arr.sum(axis=0)
    np_lst_y = np_arr.sum(axis=1)

    print([list(np_lst_y).index(np.min(np_lst_y)), list(np_lst_x).index(np.min(np_lst_x))])
    return [list(np_lst_y).index(np.min(np_lst_y)), list(np_lst_x).index(np.min(np_lst_x))]


# weak_point([[7, 2, 7, 2, 8],
#             [2, 9, 4, 1, 7],
#             [3, 8, 6, 2, 4],
#             [2, 5, 2, 9, 1],
#             [6, 6, 5, 4, 5]])
#
# weak_point([[7, 2, 4, 2, 8],
#             [2, 8, 1, 1, 7],
#             [3, 8, 6, 2, 4],
#             [2, 5, 2, 9, 1],
#             [6, 6, 5, 4, 5]])
# weak_point([[1, 1, 1],
#             [1, 1, 1],
#             [1, 1, 1]])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
