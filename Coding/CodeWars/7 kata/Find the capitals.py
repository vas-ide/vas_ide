



def capitals(word):
    result_lst = []
    for i, j in enumerate(word):
        if j == j.upper():
            result_lst.append(i)
    print(result_lst)
    return result_lst


capitals('CodEWaRs')
#[0, 3, 4, 6]


