



def columnize(items, columns_count):
    string = ""
    counter = 0
    leng_max = len(items[-1])
    for i in items:
        if columns_count > counter:
            string += f" {i:<{leng_max}} |"
            counter += 1
            if counter == columns_count:
                string = string[:-2]
                string += f'\n'
                counter = 0

    print(string)
    return string











columnize(["1", "12", "123", "1234", "12345", "123456"], 1)
columnize(["1", "12", "123", "1234", "12345", "123456"], 2)
columnize(["1", "12", "123", "1234", "12345", "123456"], 3)
columnize(["1", "12", "123", "1234", "12345", "123456"], 4)