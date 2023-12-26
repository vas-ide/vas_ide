def check_pangram(text: str) -> bool:
    dict_alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                     "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                     "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                     "y": 0, "z": 0}

    for elem in text:
        if elem.lower() in dict_alphabet:
            dict_alphabet[elem.lower()] += 1
    for value in dict_alphabet.values():
        if value < 1:
            return False

    return True



assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
assert (
    check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    == True
)
assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False
