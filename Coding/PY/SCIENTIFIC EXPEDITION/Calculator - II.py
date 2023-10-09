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
            elif len(self.string) == 1 and self.string in self.simbol_lst:
                self.result_arg = "0"
            self.result_arg = f"{int(self.string)}"
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
                        self.string_lst.append(int(digits_str))
                        digits_str = ""
                    not_digit_str += i
                if len(self.string_lst) == 2 and self.string_lst[0] == "=":
                    self.string_lst = [f"{self.string_lst[1]}"]

            if len(digits_str) > 0:
                self.string_lst.append(int(digits_str))
            elif len(not_digit_str) > 0:
                self.string_lst.append(not_digit_str)

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

            print(self.string_lst)

            if len(self.string_lst) == 2 and self.string_lst[1] in self.simbol_lst:
                self.result_arg = f"{self.string_lst[0]}"
                return self.result_arg
            elif len(self.string_lst) == 2 and len(self.string_lst[1]) > 1:
                self.result_arg = f"{self.string_lst[0]}{self.string_lst[1][0]}{self.string_lst[0]}{self.string_lst[1][1:]}"
            elif len(self.string_lst) > 2 and self.string_lst[-1] not in self.simbol_lst:
                self.result_arg = f"{self.string_lst[-1]}"
                return self.result_arg

            for i, j in enumerate(self.string_lst):
                if self.result_arg == 0 and j not in self.simbol_lst:
                    self.result_arg = j
                elif j == self.simbol_lst[0] and i != len(self.string_lst) - 1:
                    self.result_arg = f"{int(self.result_arg) + int(self.string_lst[i + 1])}"
                elif j == self.simbol_lst[1] and i != len(self.string_lst) - 1:
                    self.result_arg = f"{int(self.result_arg) - int(self.string_lst[i + 1])}"
                elif j == self.simbol_lst[2] and i != len(self.string_lst) - 1:
                    self.result_arg = f"{int(self.string_lst[i + 1])}"


def calculator(log: str) -> str:
    calc = Calculator(string=log)
    calc.run()
    print(calc.result_arg, type(calc.result_arg))
    return calc.result_arg

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
# calculator('000005+003') == '3'
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
# calculator("1+2=")
# # # "3"
# calculator("1+2-")
# # # "3"
# calculator("1+2=2")
# # # "2"
# calculator("=5=10=15")
# # "15"


