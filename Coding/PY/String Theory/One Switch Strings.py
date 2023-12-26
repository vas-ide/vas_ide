def switch_strings(line: str, result: str) -> bool:
    for elem in line:
        if line.count(elem) != result.count(elem):
            return False
    determ_counter = 0
    for number, elem in enumerate(line):
        if result[number] != elem:
            determ_counter += 1
        if determ_counter > 2:
            return False

    return True






assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True


assert switch_strings('bodep', 'bopep') == False
assert switch_strings('boss', 'bobs') == False