




def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end not in text:
        string_init = text.split(f"{begin}")
        print(f"{string_init[1]}")
        return f"{string_init[1]}"
    elif begin not in text and end in text:
        string_init = text.split(f"{end}")
        print(f"{string_init[0]}")
        return f"{string_init[0]}"
    elif begin not in text and end not in text:
        print(f"{text}")
        return f"{text}"
    elif begin in text and end in text:
        string_init = text.split(f"{begin}")
        if end in string_init[0]:
            print(f"")
            return f""
        else:
            string_init_upd = string_init[1].split(f"{end}")
        # print(string_init)
        # print(string_init_upd)
        print(string_init_upd[0])
        return f"{string_init_upd[0]}"




    # if len(string_init) < 2:
    #     return ""
    # print(string_init)
    # if end not in string_init[0] and end not in string_init[-1]:
    #     print(f"")
    #     return f""
    # string_init_upd = string_init[-1].split(f"{end}")
    # print(string_init[-1])
    # print(string_init_upd)
    # if end in string_init[0]:
    #     # print(string_init)
    #     print(f"")
    #     return f""
    # print(string_init)
    # string_init_upd = string_init[-1].split(f"{end}")
    # print(string_init_upd)
    # print(f"{string_init_upd[0]}")
    # return f"{string_init_upd[0]}"

between_markers('No <hi> one', '>', '<')
between_markers('No one', '>', '<')
print("______________Standart______________")
between_markers("What is >apple<", ">", "<")
# # "apple"
between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
# # "My new site"
between_markers("No[/b] hi", "[b]", "[/b]")
# "No"
between_markers("No [b]hi", "[b]", "[/b]")
# "hi"
between_markers("No hi", "[b]", "[/b]")
# "No hi"
between_markers("No <hi>", ">", "<")
# ""




