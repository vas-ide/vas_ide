




def computer_to_phone(numbers):
    dict_numb = {0: 0, 1: 7, 2: 8, 3: 9, 4: 4, 5: 5, 6: 6, 7: 1, 8: 2, 9: 3}
    numbers_upd = ""
    for _ in numbers:
        numbers_upd += str(dict_numb[int(_)])
    print(numbers_upd)
    return numbers_upd

computer_to_phone("0789456123")   #"0123456789"
computer_to_phone("000")          #"000"
computer_to_phone("94561")        #"34567"
computer_to_phone("")             #""
