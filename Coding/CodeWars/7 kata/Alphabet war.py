



def alphabet_war(fight):
    dict_left = {"w": 4, "p": 3, "b": 2, "s": 1}
    dict_right = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_counter = 0
    right_counter = 0
    for _ in fight:
        if _ in dict_left:
            left_counter += dict_left[_]
        elif _ in dict_right:
            right_counter += dict_right[_]
        else:
            pass
    if left_counter > right_counter:
        print(f'Left side wins!')
        return f'Left side wins!'
    elif left_counter < right_counter:
        print(f'Right side wins!')
        return f'Right side wins!'
    else:
        print(f"Let's fight again!")
        return f"Let's fight again!"











alphabet_war("z")           #"Right side wins!"
alphabet_war("zdqmwpbs")    #"Let's fight again!"
alphabet_war("wq")          #"Left side wins!"
alphabet_war("zzzzs")       #"Right side wins!"
alphabet_war("wwwwww")      #"Left side wins!"