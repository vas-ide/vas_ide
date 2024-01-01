def isometric_strings(a: str, b: str) -> bool:
    info_dict = {}
    for numb, item in enumerate(a):
        if item not in info_dict:
            info_dict[item] = b[numb]
        else:
            if info_dict[item] != b[numb]:
                return False
    return True



assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True
assert isometric_strings("all", "all") == True
assert isometric_strings("gogopy", "doodle") == False
assert isometric_strings("abba", "cccc") == True



