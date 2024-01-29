class BloodDistribution:

    def __init__(self, avaible, needs):
        self.avaible = avaible
        self.needs = needs
        self.plan = {}
        self.avaible_upd = {}
        self.needs_upd = {}
        self.dif_dict = {}
        self.dif = {}
        pass

    def calculate_blood(self):
        for key, value in self.avaible.items():
            self.avaible_upd[key] = {}
            self.needs_upd[key] = {}
            self.dif_dict[key] = {}
            for key_add, value_add in self.needs.items():
                if key == key_add:
                    self.avaible_upd[key][key_add] = value
                    self.needs_upd[key][key_add] = value_add
                    self.dif_dict[key][key_add] = (value - value_add)
                    # (value - value_add)
                    self.dif[key] = value - value_add
                else:
                    self.avaible_upd[key][key_add] = 0
                    self.needs_upd[key][key_add] = 0
                    self.dif_dict[key][key_add] = 0

    def deliver_blood(self):
        for key, value in self.dif.items():
            if value < 0:
                if key == "A":
                    if self.dif["AB"] - value >= 0:
                        differn = abs(value) - abs(self.dif["AB"])
                        self.dif["AB"] = value - differn
                        self.dif_dict["A"]["AB"] = differn
                elif key == "B":
                    if self.dif["AB"] - value >= 0:
                        differn = abs(value) - abs(self.dif["AB"])
                        self.dif["AB"] = value - differn
                        self.dif_dict["B"]["AB"] = differn
                elif key == "AB":
                    if self.dif["A"] > 0:
                        differn = self.dif["AB"] + self.dif["A"]
                        pass
                        # self.dif_dict["A"]["AB"] = self.dif["A"] - differn
                        # self.dif["AB"] = abs(self.dif["A"]) - abs(value)
                        # self.dif["A"] = abs(value) - abs(self.dif["A"])
                        # self.dif_dict["AB"]["A"] = self.dif_dict["AB"]["A"] - differn
                        print(differn)
                    elif self.dif["B"] > 0:
                        pass
                        # differn = abs(value) - abs(self.dif["B"])
                        # self.dif_dict["B"]["AB"] = self.dif["B"] - differn
                        # self.dif["AB"] = abs(self.dif["B"]) - abs(value)
                        # self.dif["B"] = abs(value) - abs(self.dif["A"])



    def run(self):
        self.calculate_blood()
        self.deliver_blood()
        self.printer()

    def printer(self):
        av = "Avaible"
        ned = "Needed"
        dif = "Difference"
        print(f"\n{av:^40}")
        [print(f"{key:<5}{value}") for key, value in self.avaible_upd.items()]
        print(f"\n{ned:^40}")
        [print(f"{key:<5}{value}") for key, value in self.needs_upd.items()]
        print(f"\n{dif:^40}")
        [print(f"{key:<5}{value}") for key, value in self.dif_dict.items()]
        print(f"\n{self.dif}")

        pass


def distribute_blood(
        blood_avail: dict[str, int], blood_needs: dict[str, int]
) -> dict[str, dict[str, int]]:
    bl = BloodDistribution(blood_avail, blood_needs)
    bl.run()


distribute_blood({"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0})
# {"A": {"A": 100, "B": 0, "AB": 50, "O": 0},
#  "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
#  "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
#  "O": {"A": 0, "B": 0, "AB": 0, "O": 0}, }


# assert distribute_blood(
#     {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}
# ) == {
#     "A": {"A": 100, "B": 0, "AB": 50, "O": 0},
#     "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
#     "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
#     "O": {"A": 0, "B": 0, "AB": 0, "O": 0},
# }
# assert distribute_blood(
#     {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
# ) == {
#     "A": {"A": 10, "B": 0, "AB": 0, "O": 0},
#     "B": {"A": 0, "B": 10, "AB": 0, "O": 0},
#     "AB": {"A": 0, "B": 0, "AB": 20, "O": 0},
#     "O": {"A": 10, "B": 0, "AB": 10, "O": 0},
# }
