




def merge_strings(first, second):
    result = first
    for _ in second:
        if _ not in first:
            result += _
    return result




















