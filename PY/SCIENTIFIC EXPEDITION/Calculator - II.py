

import re



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
                    # self.first_arg = 0
                    # self.second_arg = 0
                    self.symbol_lst = ["+", "-", "="]
                    self.symbol_arg = ""

                def init_analiz(self):
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






            cac = CalcInit(infirmation)
            cac.init_analiz()
            # cac.addition_analiz()
            print(cac.inf)
            print(cac.inf_init_analiz)
            # print(cac.inf_init_upd)
            # cac.construct()
            # print(cac.inf_construct)
            # cac.calculation()
            # print(f"{str(cac.result)}")
            # return str(cac.result)


        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")
calculator("3===+5====")
calculator("3===+====")
calculator("3+=")
# # "6"
calculator("3+2==")
# # "7"
calculator("3+-2=")
# # "1"
# calculator("-=-+3-++--+-2=-")
# # "1"
# calculator("000000")
# # "0"
# calculator("0000123")
# # "123"
# calculator("12")
# # "12"
# calculator("+12")
# # "12"
# calculator("-12")
# # "-12"
# calculator("")
# # "0"
# calculator("1+2")
# # "2"
# calculator("2+")
# # "2"
# calculator("1+2=")
# # "3"
# calculator("1+2-")
# # "3"
# calculator("1+2=2")
# # "2"
calculator("=5=10=15")
# # "15"





