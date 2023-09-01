






def longest_collatz (inputArray):
    inf_dict = dict.fromkeys(inputArray,0)
    for i in inf_dict:
        counter = 0
        target = i
        while target != 1:
            if target % 2 == 0:
                target = target / 2
                counter += 1
            else:
                target = target * 3 + 1
                counter += 1
        inf_dict[i] = counter
    key_value = max(inf_dict.values())
    rezult_dict = {key : value for key, value in inf_dict.items() if value == key_value}

    print(inf_dict, key_value,rezult_dict,list(rezult_dict)[0])
    return list(rezult_dict)[0]


longest_collatz([1, 5, 27, 4])
#27
