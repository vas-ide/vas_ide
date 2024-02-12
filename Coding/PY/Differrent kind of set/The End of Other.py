



def checkio(words_set):
    for item in words_set:
        for item_add in words_set:
            if item != item_add and item_add in item:
                if item_add == item[len(item) - len(item_add):]:
                    return True
    return False



checkio({"hello", "lo", "he"})
# == True, "helLO"
checkio({"hello", "la", "hellow", "cow"})
# == False, "hellow la cow"
checkio({"walk", "duckwalk"})
# == True, "duck to walk"
checkio({"one"})
# == False, "Only One"
checkio({"helicopter", "li", "he"})
# == False, "Only end"

assert checkio({"hello", "lo", "he"}) == True, "helLO"
assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
assert checkio({"one"}) == False, "Only One"
assert checkio({"helicopter", "li", "he"}) == False, "Only end"

