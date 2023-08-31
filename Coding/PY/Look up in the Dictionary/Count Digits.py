


def count_digits(text: str) -> int:
    counter = 0
    for i in text:
        if i.isdigit():
            counter += 1
    print(counter)
    return counter

count_digits("hi")                      #0
count_digits("who is 1st here")         #1
count_digits("my numbers is 2")         #1
count_digits("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year") #8
count_digits("5 plus 6 is")             #2
count_digits("")                        #0
