





def missing_number(items: list[int]) -> int:
    innit = "innit"
    sum = 0
    for i in sorted(items):
        if innit == "innit":
            innit = i
            sum += innit
        elif innit == 0 and i == 1:
            innit = 1
            sum += innit
        else:
            sum += innit
            if sum != i:
                print(sum)
                return sum



missing_number([1, 4, 2, 5])                    #3
missing_number([2, 6, 8, 10])                   #4
missing_number([0, 1, 3, 4, 2, 6, 9, 7, 8])     #5















