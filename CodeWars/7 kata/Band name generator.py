




def band_name_generator(name):
    if name[0] == name[-1]:
        print((name+name[1:]).capitalize())
        return (name+name[1:]).capitalize()
    else:
        print(f"The {name.capitalize()}")
        return f"The {name.capitalize()}"








band_name_generator("knife")                    #"The Knife"
band_name_generator("tart")                     #"Tartart"
band_name_generator("sandles")                  #"Sandlesandles"
band_name_generator("qq")                       #"Qqq"








