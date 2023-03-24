




def merge_strings(first, second):
    string_init = first
    result = ""
    couter = 0
    for _ in second:
        couter += 1
        if _ in first and result == "":
            result += _
        elif _ in first:
            result += _
            if result not in first:
                pass
    return result




















