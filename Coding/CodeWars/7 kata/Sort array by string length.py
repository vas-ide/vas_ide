



def sort_by_length(arr):
    num_dic = {}
    for i in arr:
        num_dic[i] = len(i)
    sorted_dic = dict(sorted(num_dic.items(), key=lambda item: item[1]))
    print(list(sorted_dic.keys()))
    return list(sorted_dic.keys())



sort_by_length(["beg", "life", "i", "to"])                                              #["i", "to", "beg", "life"],
sort_by_length(["", "moderately", "brains", "pizza"])                                   #["", "pizza", "brains", "moderately"]
sort_by_length(["longer", "longest", "short"])                                          #["short", "longer", "longest"]
sort_by_length(["dog", "food", "a", "of"])                                              #["a", "of", "dog", "food"]
sort_by_length(["", "dictionary", "eloquent", "bees"])                                  #["", "bees", "eloquent", "dictionary"]
sort_by_length(["a longer sentence", "the longest sentence", "a short sentence"])       #["a short sentence", "a longer sentence", "the longest sentence"]




# def sort_by_length(arr):
#     return sorted(arr, key=len)