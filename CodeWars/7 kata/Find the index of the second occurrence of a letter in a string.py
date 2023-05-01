


def second_symbol(s, symbol):
    counter = 0
    for i, j in enumerate(s):
        if j == symbol:
            if counter == 0:
                counter = 1
            elif counter == 1:
                return i
    return -1