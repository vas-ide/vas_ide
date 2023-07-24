



def duplicate_count(text):
    data_dict = {}
    counter_dub = 0
    for i in text.lower():
        if i in data_dict:
            data_dict[i] += 1
        else:
            data_dict[i] = 1
    for i in data_dict.values():
        if i > 1:
            counter_dub += 1

    print(data_dict, counter_dub)
    return counter_dub

duplicate_count("")#0
duplicate_count("abcde")#0
duplicate_count("abcdeaa")#1
duplicate_count("abcdeaB")#2
duplicate_count("Indivisibilities")#2

