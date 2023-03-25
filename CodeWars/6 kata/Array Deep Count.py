



count = []
def deep_count(a):
    global count
    for i in a:
        count.append(1)
        if type(i) == list:
            deep_count(i)
    print(len(count))
    return len(count)









deep_count([])                          #0
deep_count([1, 2, 3])                   #3
deep_count(["x", "y", ["z"]])           #4
deep_count([1, 2, [3, 4, [5]]])         #7
deep_count([[[[[[[[[]]]]]]]]])          #8









