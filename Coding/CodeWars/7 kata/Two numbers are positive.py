def two_are_positive(a, b, c):
    counter = 0
    if a > 0:
        counter += 1
    if b > 0:
        counter += 1
    if c > 0:
        counter += 1
    if counter == 2:
        return True
    return False