import numpy as np


def checkio(matrix):
    np_arr = np.array(matrix)
    # print(np_arr)
    # if list(np_arr) == list(np.rot90(np_arr, 2)):
    #     print(True)
    #     return True
    # print(False)
    # return False
    # print(np_arr)
    for item in range(len(np_arr)):
        print(abs(list(np_arr)[item]))
        print(abs(list(np.rot90(np_arr, 2))[item]))
        if abs(list(np_arr)[item]) == abs(list(np.rot90(np_arr, 2))[item]):
            print("11111")
        # if list(np_arr)[item] != list(np.rot90(np_arr, 2))[item]:
        #     print(False)
    # print(True)
    #     print(item)
    # print(len((np_arr)))
    # for i in len
    # if list(abs(np_arr)) == list(abs(np.rot90(np_arr, 2))):
    #     print(f"!!!")
    # print(f"____")
    # print(abs(np.rot90(np_arr, 2)))
    # try:
    #     np_arr_upd = np.linalg.inv(np_arr)
    #     print(np.sum(np_arr))
    #     # print(np_arr_upd)
    #     if np.sum(np_arr) == 0:
    #         print(True)
    #         return True
    #     else:
    #         print(False)
    #         return False
    # except:
    #     print(True)
    #     return True
# checkio([[-8,5,-1,7,0],[-5,-5,-7,-6,8],[1,7,1,3,4],[-7,6,-3,5,-4],[0,-8,-4,4,7]])
# checkio([[0,1,2,3,4],[-1,0,5,6,7],[-2,-5,0,8,9],[-3,-6,-8,0,0],[-4,-7,-9,0,0]])
# #
checkio([
    [0, 1, 2],
    [-1, 0, 1],
    [-2, -1, 0]])
# checkio([
#     [0, 1, 2],
#     [-1, 1, 1],
#     [-2, -1, 0]])
# checkio([
#     [0, 1, 2],
#     [-1, 0, 1],
#     [-3, -1, 0]])

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
