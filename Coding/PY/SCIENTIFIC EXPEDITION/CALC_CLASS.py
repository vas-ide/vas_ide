import re


class  Calculator():

    def __init__(self, string):
        self.string = string
        self.simbol_lst = ["+", "-", "="]
        self.string_lst = []
        self.before_arg = ""
        self.after_arg = ""
        self.result_arg = ""
    def run(self):
        try:
            if len(self.string) < 1:
                print(f"0")
                return f"0"
            print(f"{int(self.string)}")
            return f"{int(self.string)}"
        except:
            digits_str = ''
            not_digit_str = ""
            for i in self.string:
                if i not in self.simbol_lst:
                    if len(not_digit_str) > 0:
                        self.string_lst.append(not_digit_str)
                        not_digit_str = ""
                    digits_str += i
                elif i in self.simbol_lst:
                    if len(digits_str) > 0:
                        self.string_lst.append(digits_str)
                        digits_str = ""
                    not_digit_str += i
                if len(self.string_lst) == 2 and self.string_lst[0] == "=":
                    self.string_lst = [f"{self.string_lst[1]}"]

            if len(digits_str) > 0:
                self.string_lst.append(digits_str)
            elif len(not_digit_str) > 0:
                    self.string_lst.append(not_digit_str)
            if self.string_lst[0] in self.simbol_lst:
                pass


            print(self.string_lst)



            if len(self.string_lst) == 2 and self.string_lst[1] in self.simbol_lst:
                print(self.string_lst[0])
                return self.string_lst[0]
            elif len(self.string_lst) == 3 and self.string_lst[1] in self.simbol_lst:
                print(self.string_lst[2])
                return self.string_lst[2]

            for i, j in enumerate(self.string_lst):
                if j == self.simbol_lst[0] and i != len(self.string_lst) - 1:
                    if self.result_arg == 0:
                        self.result_arg = self.string_lst[i - 1] = self.string_lst[i + 1]
                        print(self.result_arg)


            print(self.result_arg)


def calculator(log: str) -> str:
    calc = Calculator(string=log)
    calc.run()


# def calculator(log: str) -> str:
#     match log:
#         case str(information) if len(information) < 1:
#             print(f"0")
#             return f"0"
#
#
#         case str(infirmation):
#             class CalcInit:
#                 def __init__(self, inf):
#                     self.inf = inf
#                     self.inf_upd = []
#                     self.result = 0
#                     self.more_arg = ""
#                     self.first_arg = 0
#                     self.second_arg = 0
#                     self.symbol_lst = ["+", "-", "="]
#
#
#                 def analize(self):
#                     if len(self.inf) == 1 and self.inf[0] in self.symbol_lst:
#                         self.inf_upd.append(0)
#                     else:
#                         for _, __ in enumerate(self.inf):
#                             if len(self.inf) == 1 and __ in self.symbol_lst:
#                                 self.inf_upd.append(0)
#                             elif __ == " ":
#                                 pass
#                             elif __ in self.symbol_lst and len(self.more_arg) < 1:
#                                 if __ == "-":
#                                     self.more_arg += __
#                                 # else:
#                                 #     pass
#                             elif __ not in self.symbol_lst:
#                                 self.more_arg += __
#                             elif __ in self.symbol_lst and _ == len(self.inf) - 1:
#                                 pass
#                             elif __ in self.symbol_lst and len(self.more_arg) >= 1:
#                                     self.inf_upd.append(int(self.more_arg))
#                                     self.inf_upd.append(__)
#                                     self.more_arg = ""
#                         self.inf_upd.append(int(self.more_arg))
#                         if __ in self.symbol_lst and _ == len(self.inf) - 1:
#                             self.inf_upd.append(__)
#
#
#
#
#                 def calculation(self):
#                     if len(self.inf_upd) == 1:
#                         self.result = str(self.inf_upd[0])
#                     else:
#                         self.result = self.inf_upd[0]
#                         for _, __ in enumerate(self.inf_upd):
#                             if __ == "+" and len(self.inf_upd) >= _ + 3:
#                                 if self.inf_upd[_ + 2] in self.symbol_lst:
#                                     self.result += self.inf_upd[_ + 1]
#                             elif __ == "+" and len(self.inf_upd) >= _ + 2:
#                                 self.result = self.inf_upd[_ + 1]
#                             elif __ == "-" and len(self.inf_upd) >= _ + 3:
#                                 if self.inf_upd[_ + 2] in self.symbol_lst:
#                                     self.result -= self.inf_upd[_ + 1]
#                             elif __ == "-" and len(self.inf_upd) >= _ + 2:
#                                 self.result = self.inf_upd[_ + 1]
#                             elif __ == "-" and len(self.inf_upd) >= _ + 4:
#                                 self.result = self.inf_upd[_ + 3]
#                             elif __ == "=" and len(self.inf_upd) >= _ + 3:
#                                 if self.inf_upd[_ + 2] in self.symbol_lst:
#                                     self.result = self.inf_upd[_ + 1]
#                             if __ == "=" and len(self.inf_upd) == _ + 2:
#                                 self.result = self.inf_upd[_ + 1]
#             cac = CalcInit(infirmation)
#             cac.analize()
#             print((f"{cac.inf_upd}"))
#             cac.calculation()
#             print(f"{str(cac.result)}")
#             return str(cac.result)
#
#
#         case _:
#             print(f"Непредвиденная ошбка нуэен дополнительный анализ.")

#
# calculator("-25")
# calculator("000000")
# # # "0"
# calculator("0000123")
# # # "123"
# calculator("12")
# # # "12"
# calculator("+12")
# # # "12"
# calculator("")
# # # "0"
# calculator("1+2")
# # # "2"
# calculator("2+")
# # "2"
calculator("1+2=")
# # "3"
calculator("1+2-")
# # "3"
calculator("1+2=2")
# # "2"
calculator("=5=10=15")
# # "15"




