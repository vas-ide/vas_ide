


def lcs(x, y):

    if y in x:
        print(y)
        return y
    else:
        max_, min_ = x, y
        if len(y) > len(x):
            max_, min_ = y, x
        result = ""
        for _, __ in enumerate(min_):
            if __ in max_[_:]:
                if x.count(__) > result.count(__):
                    result += __
        print(result)
        return result

        #     result += f'{_.count(x)}'
        # print(result)
        #     # if _ in x:
        #     #
        #     #     # if _.count(result)
        #









lcs("a", "b")                           #""
lcs("a", "a")                           #"a"
lcs("abc", "ac")                        #"ac"
lcs("abcdef", "abc")                    #"abc"
lcs("abcdef", "acf")                    #"acf"
lcs("anothertest", "notatest")          #"nottest"
lcs("anothertest", "notatest")          #"nottest"
lcs("132535365", "123456789")           #"12356"
lcs("finaltest", "zzzfinallyzzz")       #"final"



