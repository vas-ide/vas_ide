
import re




def calculator(txt):
    if "+" in txt:
        lst = txt.split("+")
        print("." * int((len(lst[0]) - 1) + (len(lst[1]) - 1)))
        return "." * int((len(lst[0]) - 1) + (len(lst[1]) - 1))
    elif "-" in txt:
        lst = txt.split("-")
        print("." * int((len(lst[0]) - 1) - (len(lst[1]) - 1)))
        return "." * int((len(lst[0]) - 1) - (len(lst[1]) - 1))
    elif "*" in txt:
        lst = txt.split("*")
        print("." * int((len(lst[0]) - 1) * (len(lst[1]) - 1)))
        return "." * int((len(lst[0]) - 1) * (len(lst[1]) - 1))
    elif "//" in txt:
        lst = txt.split("//")
        print("." * int((len(lst[0]) - 1) // (len(lst[1]) - 1)))
        return "." * int((len(lst[0]) - 1) // (len(lst[1]) - 1))







calculator("..... + ...............")           #"...................."
calculator("..... - ...")                       #".."
calculator("..... - .")                         #"...."
calculator("..... * ...")                       #"..............."
calculator("..... * ..")                        #".........."
calculator("..... // ..")                       #".."
calculator("..... // .")                        #"....."
calculator(". // ..")                           #""
calculator(". - .")                             #""



