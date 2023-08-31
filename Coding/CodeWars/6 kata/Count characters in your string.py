




def count(string):
    result = {}
    # for i in string:
    #     if i not in result:
    #         result[i] = 1
    #     else:
    #         result[i] += 1
    # The function code should be here
    for char in string:
        result[char] = result.get(char, 0) + 1
    print(result)
    return result















count('aba')            #{'a': 2, 'b': 1}
count('')               #{}




