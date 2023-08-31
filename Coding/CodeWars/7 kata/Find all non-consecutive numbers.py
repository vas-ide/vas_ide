




def all_non_consecutive(arr):
    mark = "init"
    lst_result = []
    for _, __ in enumerate(arr):
        if mark == "init":
            mark = __
        else:
            if __ == arr[_ - 1] + 1:
                pass
            else:
                lst_result.append({"i": _, "n": __})

    print(lst_result)
    return lst_result













all_non_consecutive([1,2,3,4,6,7,8,10])         #[{'i': 4, 'n': 6}, {'i': 7, 'n': 10}]

