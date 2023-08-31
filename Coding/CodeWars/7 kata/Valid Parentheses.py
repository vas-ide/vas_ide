



def valid_parentheses(paren_str):
    counter_open = 0
    counter_closed = 0
    for _, __ in enumerate(paren_str):
        if __ == "(":
            counter_open += 1
        elif __ == ")":
            counter_closed += 1
        if counter_closed > counter_open:
            return False
    if counter_open == counter_closed:
        return True
    else:
        return False






valid_parentheses("()()(")
valid_parentheses("((())")



