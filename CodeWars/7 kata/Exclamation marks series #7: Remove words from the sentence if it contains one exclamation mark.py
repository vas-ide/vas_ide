



def remove(s):
    lst = s.split(" ")
    result = ""
    for i in lst:
        if i.count(f"!") != 1:
            result += f"{i} "
    print(result[:-1])
    return result[:-1]






remove('Hi!')                       #''
remove('Hi!!!')                     #'Hi!!!'
remove('!Hi')                       #''
remove('!Hi!')                      #'!Hi!'
remove('Hi! Hi!')                   #''
remove('!!!Hi !!hi!!! !hi')         #'!!!Hi !!hi!!!'
remove('!Hi! ! !Hi!')               #'!Hi! !Hi!'





