def safe_pawns(pawns: set) -> int:
    line = ["a", "b", "c", "d", "e", "f", "g", "h"]
    counter = 0
    for item in pawns:
        if item[0] == "a" and int(item[1]) > 1:
            if f"b{int(item[1]) - 1}" in pawns:
                counter += 1
        elif item[0] == "h" and int(item[1]) > 1:
            if f"g{int(item[1]) - 1}" in pawns:
                counter += 1
        elif int(item[1]) > 1:
            line_index = line.index(item[0])
            if f"{line[line_index + 1]}{int(item[1]) - 1}" in pawns:
                counter += 1
            elif f"{line[line_index - 1]}{int(item[1]) - 1}" in pawns:
                counter += 1
    return counter


# line.index(item[0])
#     if f"{}{item[1] - 1}" in pawns:
#         counter += 1


safe_pawns({"c4", "d3"})
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
safe_pawns({'f6', 'e5', 'd4', 'h8', 'g7', 'a1', 'b2', 'c3'})

#
assert safe_pawns({'f6', 'e5', 'd4', 'h8', 'g7', 'a1', 'b2', 'c3'}) == 7
assert safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}) == 6
assert safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}) == 1
#
