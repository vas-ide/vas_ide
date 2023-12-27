def checkio(data: str) -> bool:
    match data:
        case str() as password if len(password) >= 10:
            counter_digit = 0
            counter_normal = 0
            counter_caps = 0
            for item in password:
                if item.isalpha():
                    if item == item.lower():
                        counter_normal += 1
                    elif item == item.upper():
                        counter_caps += 1
                elif item.isdigit():
                    counter_digit += 1
            if counter_caps > 0 and counter_normal > 0 and counter_digit > 0:
                return True
            else:
                return False

        case _:
            print(F"Неправильный формат данных")
            return False


# def column_number(cmd):
#     match cmd:
#         case str() as command if len(command) == 1:
#             print(f"{int(alphabet_exel[command])}")
#             return int(alphabet_exel[command])
#         case str() as command if len(command) > 1:
#             total = 0
#             degree = len(command) - 1
#             for i in command:
#                 if i != command[-1]:
#                     total += alphabet_exel[i] * 26 ** degree
#                     print(alphabet_exel[i], degree, 26)
#                     degree -= 1
#                 elif i == command[-1]:
#                     total += alphabet_exel[i]
#             print(total)
#             return int(total)
# checkio("Icao2014")
# checkio("Icao20142014")
assert checkio("ULFFunH8ni") == True
assert checkio("aaaaaaaaaaaaaaaaaaaaa") == False
assert checkio("aA1") == False
assert checkio("awzbdzkfz") == False
assert checkio("RCAGOSHTTS") == False
assert checkio("6691219721") == False
assert checkio("PVlppfwrT") == False
assert checkio("45ae5lkgz") == False
assert checkio("1cmuPF1Ycz") == True
assert checkio("Pv4HdnUNb") == False
assert checkio("jRNfXg6CdM15SLChALq") == True
assert checkio("HZeLrcRR3NU5KprAybp") == True
assert checkio("aaaaaaaaaa1A") == True
assert checkio("aaaaaaaaa1Za") == True
assert checkio("aaaaaaaaa9Aa") == True
assert checkio("AAAAAAAAA1zA") == True
