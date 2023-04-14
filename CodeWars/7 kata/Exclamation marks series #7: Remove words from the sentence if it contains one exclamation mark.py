



def remove(s):
    counter = 0
    new_word = ""
    result = ""
    for i in s:
        if i == " ":
            if counter != 1:
                result += new_word
            new_word = ""
            counter = 0
        elif i == "!":
            counter += 1
            new_word += i
        else:
            new_word += i
    if len(new_word) > 0 and counter != 1:
        result += new_word
    print(result)
    return result





remove('Hi!')                       #''
remove('Hi!!!')                     #'Hi!!!'
remove('!Hi')                       #''
remove('!Hi!')                      #'!Hi!'
remove('Hi! Hi!')                   #''
remove('!!!Hi !!hi!!! !hi')         #'!!!Hi !!hi!!!'
remove('!Hi! ! !Hi!')               #'!Hi! !Hi!'





