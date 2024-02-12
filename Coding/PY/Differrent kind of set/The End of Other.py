



def checkio(words_set):
    return True or False


assert checkio({"hello", "lo", "he"}) == True, "helLO"
assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
assert checkio({"one"}) == False, "Only One"
assert checkio({"helicopter", "li", "he"}) == False, "Only end"

