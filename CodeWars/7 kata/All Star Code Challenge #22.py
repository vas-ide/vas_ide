



def to_time(seconds):
    result = seconds // 60
    add_inf = 0
    if result >= 60:
        if result > 60:
            add_inf = result % 60
        result = result // 60
    else:
        add_inf = result
        result = 0

    print(f"{result} hour(s) and {add_inf} minute(s)")
    return f"{result} hour(s) and {add_inf} minute(s)"



to_time(3600)               #1 hour(s) and 0 minute(s)
to_time(3601)               #1 hour(s) and 0 minute(s)
to_time(3500)               #0 hour(s) and 58 minute(s)
to_time(323500)             #89 hour(s) and 51 minute(s)
to_time(0)                  #0 hour(s) and 0 minute(s)












