


def race_podium(blocks):
    level = blocks // 3 - 1
    additionals_blocks = blocks - level * 3
    if blocks == 7:
        print((2,4,1))
        return (2,4,1)

    if additionals_blocks == 3:
        print((level + 1, level + 2, level))
        return (level + 1, level + 2, level)
    elif additionals_blocks == 4:
        print((level + 2, level + 3, level - 1))
        return (level + 2, level + 3, level - 1)
    elif additionals_blocks == 5:
        print((level + 2, level + 3, level))
        return (level + 2, level + 3, level)


race_podium(11)         #(4,5,2)
race_podium(6)          #(2,3,1)
race_podium(10)         #(4,5,1)
race_podium(100000)     #(33334,33335,33331)
race_podium(7)          #(2,4,1)
race_podium(8)          #(3,4,1)



