import numpy as np


def checkio(matrix):
    np_arr = np.array(matrix)
    print(np_arr)
    try:
        np_arr_upd = np.linalg.inv(np_arr)
        print(False)
        print(np_arr_upd)
        print(np_arr.dot(np_arr_upd))
        print(np.matmul(np_arr, np_arr_upd))
        return False
    except:
        print(True)
        return True

# checkio([[0,1,2,3,4],[-1,0,5,6,7],[-2,-5,0,8,9],[-3,-6,-8,0,0],[-4,-7,-9,0,0]])
#
# checkio([
#     [0, 1, 2],
#     [-1, 0, 1],
#     [-2, -1, 0]])
# checkio([
#     [0, 1, 2],
#     [-1, 1, 1],
#     [-2, -1, 0]])
checkio([
    [0, 1, 2],
    [-1, 0, 1],
    [-3, -1, 0]])

# a = np.array([[1, 2, 1], [1, 1, 4], [2, 3, 6]], dtype=np.float32)
# b = np.linalg.inv(a)
#
# print ("Матрица A:\n", a)
# print ("Обратная матрица к A:\n", b)
# print ("Произведение A на обратную должна быть единичной:\n", a.dot(b))

# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     # print("Example:")
#     # print(checkio([
#     #     [0, 1, 2],
#     #     [-1, 0, 1],
#     #     [-2, -1, 0]]))
#
#     assert checkio([
#         [0, 1, 2],
#         [-1, 0, 1],
#         [-2, -1, 0]]) == True, "1st example"
#     assert checkio([
#         [0, 1, 2],
#         [-1, 1, 1],
#         [-2, -1, 0]]) == False, "2nd example"
#     assert checkio([
#         [0, 1, 2],
#         [-1, 0, 1],
#         [-3, -1, 0]]) == False, "3rd example"
#     print("Coding complete? Click 'Check' to earn cool rewards!");
