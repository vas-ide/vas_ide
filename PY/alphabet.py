


# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[0]))               # Алфавит
# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[0], reverse=True)) # Алфавит в обратном порядке
# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[1], reverse=True)) # ТОТАЛ
dict_alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                 "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                 "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                 "y": 0, "z": 0,
                 "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0,
                 "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0,
                 "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                 "Y": 0, "Z": 0}
dict_alphabet_reverse = {"z": 0, "y": 0, "x": 0, "w": 0, "v": 0, "u": 0, "t": 0, "s": 0,
                         "r": 0, "q": 0, "p": 0, "o": 0, "n": 0, "m": 0, "l": 0, "k": 0,
                         "j": 0, "i": 0, "h": 0, "g": 0, "f": 0, "e": 0, "d": 0, "c": 0,
                         "b": 0, "a": 0,
                         "Z": 0, "Y": 0, "X": 0, "W": 0, "V": 0, "U": 0, "T": 0, "S": 0,
                         "R": 0, "Q": 0, "P": 0, "O": 0, "N": 0, "M": 0, "L": 0, "K": 0,
                         "J": 0, "I": 0, "H": 0, "G": 0, "F": 0, "E": 0, "D": 0, "C": 0,
                         "B": 0, "A": 0}
def printer(dict):
    print(f"+---------+---------+")
    print(f"|  Буква  | Частота |")
    print(f"+---------+---------+")
    # print(dict_stat)
    tootal = 0
    for key, value in dict.items():
        print(f"|{key:^9}|{value:^9}|")
        tootal += value
    print(f"+---------+---------+")
    print(f"|  Итого  |{tootal:^9}|")
    print(f"+---------+---------+")





