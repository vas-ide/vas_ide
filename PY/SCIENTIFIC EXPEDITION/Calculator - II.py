def calculator(log: str) -> str:
    match log:
        case str(information) if len(information) < 1:
            print(f"0")
            return f"0"

        case str(infirmation):
            class CalcInit:
                def __init__(self, inf):
                    self.inf = inf
                    self.inf_init_analiz = []
                    # self.inf_init = []
                    # self.inf_init_upd = []
                    # self.inf_construct = []
                    # self.inf_upd = []
                    # self.result = 0
                    self.number_arg = ""
                    self.more_arg = ""
                    # self.more_arg_add = ""
                    self.first_arg = 0
                    self.second_arg = 0
                    self.result_arg = 0
                    self.symbol_lst = ["+", "-", "="]
                    self.symbol_arg = ""
                    self.symbol_arg_add = ""

                def init_analiz(self):
                    # first
                    for _, __ in enumerate(self.inf):
                        if len(self.inf_init_analiz) < 1:
                            if __ in self.symbol_lst and len(self.number_arg) < 1:
                                self.symbol_arg = __
                            elif __.isdigit():
                                self.number_arg += __
                            elif __ in self.symbol_lst:
                                if self.symbol_arg != self.symbol_lst[1]:
                                    self.symbol_arg = ""
                                self.inf_init_analiz.append(f"{self.symbol_arg}{self.number_arg}")
                                self.symbol_arg = __
                                self.number_arg = ""

                        # all
                        else:
                            if __ in self.symbol_lst:
                                if len(self.number_arg) > 0:
                                    self.inf_init_analiz.append(self.number_arg)
                                    self.number_arg = ""
                                self.symbol_arg += __
                            elif __.isdigit():
                                if len(self.symbol_arg) > 0:
                                    self.inf_init_analiz.append(self.symbol_arg)
                                    self.symbol_arg = ""
                                self.number_arg += __

                    # final
                    if len(self.number_arg) > 0:
                        if self.symbol_arg != self.symbol_lst[1]:
                            self.symbol_arg = ""
                        self.inf_init_analiz.append(f"{self.symbol_arg}{int(self.number_arg)}")
                        self.symbol_arg = ""
                        self.number_arg = ""
                    elif len(self.symbol_arg) > 0:
                        self.inf_init_analiz.append(f"{self.symbol_arg}")
                        self.symbol_arg = ""
                        self.number_arg = ""

                    if len(self.inf_init_analiz) > 1 and len(self.inf_init_analiz[1]) != 1:
                        for i in self.inf_init_analiz[1]:
                            if i == self.symbol_lst[2] and len(self.symbol_arg) < 1:
                                pass
                            elif i != self.symbol_lst[2]:
                                self.symbol_arg = i
                            else:
                                self.symbol_arg += i
                        self.inf_init_analiz[1] = self.symbol_arg
                        self.symbol_arg = ""

                def calculate(self):

                    for _, __ in enumerate(self.inf_init_analiz):
                        if len(self.inf_init_analiz) == 1:
                            self.result_arg = int(self.inf_init_analiz[0])
                        elif len(self.inf_init_analiz) == 2:
                            if len(self.inf_init_analiz[1]) > 1 and self.inf_init_analiz[1][0] == self.symbol_lst[0]:
                                counter = 1
                                while counter <= len(self.inf_init_analiz[1]):
                                    self.result_arg += int(self.inf_init_analiz[0])
                                    counter += 1
                                break
                            elif len(self.inf_init_analiz[1]) > 1 and self.inf_init_analiz[1][0] == self.symbol_lst[1]:
                                counter = 1
                                while counter <= len(self.inf_init_analiz[1]):
                                    self.result_arg -= int(self.inf_init_analiz[0])
                                    counter += 1
                                break
                            else:
                                self.result_arg = int(self.inf_init_analiz[0])



                        elif len(self.inf_init_analiz) == 3:
                            self.result_arg = int(self.inf_init_analiz[-1])
                        elif len(self.inf_init_analiz) >= 4:
                            if len(__) == 1 and len(self.inf_init_analiz) >= (_ + 2):
                                if __ == self.symbol_lst[0]:
                                    self.first_arg = self.inf_init_analiz[_ - 1]
                                    self.second_arg = self.inf_init_analiz[_ + 1]
                                    self.result_arg += int(self.first_arg) + int(self.second_arg)
                                elif __ == self.symbol_lst[1]:
                                    self.first_arg = self.inf_init_analiz[_ - 1]
                                    self.second_arg = self.inf_init_analiz[_ + 1]
                                    self.result_arg += int(self.first_arg) - int(self.second_arg)
                                    self.symbol_arg_add = self.symbol_lst[1]
                                elif __ == self.symbol_lst[2]:
                                    self.result_arg = (self.inf_init_analiz[_ + 1])


                            elif len(__) > 1 and len(self.inf_init_analiz) == (_ + 1):
                                if __[0] == self.symbol_lst[0]:
                                    self.second_arg = self.inf_init_analiz[_ - 1]
                                    for i in __[1:]:
                                        if i != self.symbol_lst[2]:
                                            break
                                        else:
                                            self.result_arg += int(self.second_arg)
                                elif __[0] == self.symbol_lst[1]:
                                    self.second_arg = self.inf_init_analiz[_ - 1]
                                    for i in __[1:]:
                                        if i != self.symbol_lst[2]:
                                            break
                                        else:
                                            self.result_arg -= int(self.second_arg)
                                elif __[0] == self.symbol_lst[2]:
                                    self.second_arg = self.inf_init_analiz[_ - 1]
                                    if self.symbol_arg_add == self.symbol_lst[1]:
                                        for i in __[1:]:
                                            if i != self.symbol_lst[2]:
                                                break
                                            else:
                                                self.result_arg -= int(self.second_arg)
                                    else:
                                        for i in __[1:]:
                                            if i != self.symbol_lst[2]:
                                                break
                                            else:
                                                self.result_arg += int(self.second_arg)
                                        break

            cac = CalcInit(infirmation)
            cac.init_analiz()
            cac.calculate()
            # print(cac.inf)
            print(cac.inf_init_analiz)
            print(cac.result_arg)
            # return f"{cac.result_arg}"

        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")



calculator("3+=")
# "6"
calculator("3+2==")
# # "7"
# calculator("3+-2=")
# # "1"
calculator("-=-+3-++--+-2=-")
# # # "1"
# calculator("000000")
# # # "0"
# calculator("0000123")
# # # "123"
# calculator("12")
# # # "12"
# calculator("+12")
# # # "12"
# calculator("-12")
# # # "-12"
# calculator("")
# # "0"
# calculator("1+2")
# "2"
# calculator("2+")
# # # "2"
# calculator("1+2=")
# # # "3"
# calculator("1+2-")
# # # "3"
# calculator("1+2=2")
# # # "2"
# calculator("=5=10=15")
# # # "15"
