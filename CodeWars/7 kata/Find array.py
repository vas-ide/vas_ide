


def find_array(arr1, arr2):
    rezult = []
    if len(arr1) < 1 or len(arr2) < 1:
        return rezult
    else:
        for i in arr2:
            if i >= len(arr1):
                return []
            rezult.append(arr1[i])
    print(rezult)
    return rezult








find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7])
# [1, 1, 1]

