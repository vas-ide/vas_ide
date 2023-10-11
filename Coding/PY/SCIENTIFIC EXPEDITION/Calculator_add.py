class Calculator:

    def __init__(self, string):
        self.string = string
        self.simbol_lst = ["+", "-", "="]
        self.string_lst = []
        self.before_arg = ""
        self.after_arg = ""
        self.result_arg = 0
        self.upd_simbol = ""


    def run(self):
        try:
            if len(self.string) < 1:
                self.result_arg = "0"
                return self.result_arg
            elif len(self.string) == 1 and self.string in self.simbol_lst:
                self.result_arg = "0"
            self.result_arg = f"{int(self.string)}"
            return self.result_arg
        except:
            self.analiz_list(self.string)
            self.analiz_simbol()


            if len(self.string_lst) == 2 and self.string_lst[1] in self.simbol_lst:
                self.result_arg = f"{self.string_lst[0]}"
                return self.result_arg
            elif len(self.string_lst) == 2 and len(self.string_lst[1]) > 1:
                self.string = f"{self.string_lst[0]}{self.string_lst[1][0]}{self.string_lst[0]}{self.string_lst[1][1:]}"
                self.analiz_list(self.string)
            elif len(self.string_lst) > 2 and type(self.string_lst[-1]) == int:
                self.result_arg = f"{self.string_lst[-1]}"
                return self.result_arg
            if len(self.string_lst[-1]) >= 2:
                self.string = ""
                add_str = f"{self.string_lst[-3]}{self.string_lst[-2]}"*(len(self.string_lst[-1]) - 1)
                for i in self.string_lst:
                    if i != self.string_lst[-1]:
                        self.string += f"{i}"
                self.string += add_str + "="
                self.analiz_list(self.string)

            self.calc_result()

    def calc_result(self):
        for i, j in enumerate(self.string_lst):
            if self.result_arg == 0 and j not in self.simbol_lst:
                self.result_arg = j
            elif j == self.simbol_lst[0] and i != len(self.string_lst) - 1:
                self.result_arg = f"{int(self.result_arg) + int(self.string_lst[i + 1])}"
            elif j == self.simbol_lst[1] and i != len(self.string_lst) - 1:
                self.result_arg = f"{int(self.result_arg) - int(self.string_lst[i + 1])}"
            elif j == self.simbol_lst[2] and i != len(self.string_lst) - 1:
                self.result_arg = f"{int(self.string_lst[i + 1])}"

    def analiz_simbol(self):
        for i, j in enumerate(self.string_lst):
            if type(j) == str and len(j) > 1:
                if i != len(self.string_lst) - 1:
                    self.string_lst[i] = j[-1]
                else:
                    for k in j:
                        if len(self.upd_simbol) < 1:
                            self.upd_simbol = k
                        else:
                            if len(self.upd_simbol) > 0 and k != self.simbol_lst[2]:
                                self.upd_simbol = k
                            else:
                                self.upd_simbol += k
                    self.string_lst[i] = self.upd_simbol


        # if len(self.string_lst) > 2 and len(self.string_lst[-1]) > 1:
        #     self.upd_simbol = ""
        #     for k in self.simbol_lst[-1]:
        #         if len(self.upd_simbol) < 1 and k != self.simbol_lst[2]:
        #             self.result_arg = f"0"
        #             return self.result_arg
        #         else:
        #             if k == self.simbol_lst[2]:
        #                 self.upd_simbol += k
        #     self.string_lst[i] = self.upd_simbol


    def analiz_list(self, string_info):
        self.string_lst = []
        digits_str = ''
        not_digit_str = ""
        for i in string_info:
            if i not in self.simbol_lst:
                if len(not_digit_str) > 0:
                    self.string_lst.append(not_digit_str)
                    not_digit_str = ""
                digits_str += i
            elif i in self.simbol_lst:
                if len(digits_str) > 0:
                    self.string_lst.append(int(digits_str))
                    digits_str = ""
                not_digit_str += i
            if len(self.string_lst) == 2 and self.string_lst[0] == "=":
                self.string_lst = [f"{self.string_lst[1]}"]
        if len(digits_str) > 0:
            self.string_lst.append(int(digits_str))
        elif len(not_digit_str) > 0:
            self.string_lst.append(not_digit_str)


def calculator(log: str) -> str:
    calc = Calculator(string=log)
    calc.run()
    print(calc.result_arg, type(calc.result_arg))
    return calc.result_arg
calculator('3+2-=')
# 0
calculator("3+2====")
# 11
calculator("3+==")
# 9
calculator("3+=")
# "6"
calculator("3+2==")
# "7"
calculator("4-1==")
# "2"
calculator("3+-2=")
# "1"
calculator("-=-+3-++--+-2=-")
# "1"
calculator('-5-10+15')
calculator('000005+003') == '3'
calculator("-25")
# calculator("000000")
# # # "0"
# calculator("0000123")
# # # "123"
# calculator("12")
# # # "12"
# calculator("+12")
# # # "12"
calculator("")
# # # "0"
# calculator("1+2")
# # # "2"
# calculator("2+")
# # "2"
# calculator("1+2=")
# # # "3"
# calculator("1+2-")
# # # "3"
# calculator("1+2=2")
# # # "2"
# calculator("=5=10=15")
# # "15"


