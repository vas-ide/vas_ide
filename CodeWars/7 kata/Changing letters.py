





def swap(st):
    vowels_arr = ("a", "e", "i", "o", "u")
    rez = ""
    for _ in st:
        if _.lower() in vowels_arr:
            rez += _.upper()
        else:
            rez += _
    print(rez)
    return rez

# def swap(st):
#     return "".join( c.upper() if c in "aeiou" else c for c in st )


swap("HelloWorld!")         #"HEllOWOrld!"
swap("Sunday")              #"SUndAy"
swap("Codewars")            #"COdEwArs"
swap("Monday")              #"MOndAy"
swap("Friday")              #"FrIdAy"
swap("abracadabra")         #"AbrAcAdAbrA"



