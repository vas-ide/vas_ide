class BloodDistribution:

    def __init__(self, avaible, needs):
        self.avaible = avaible
        self.needs = needs
        self.avaible_upd = {}
        self.needs_upd = {}
        self.dif_dict = {}
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
                    self.dif_dict[key][key_add] = value - value_add
                else:
                    self.avaible_upd[key][key_add] = 0
                    self.needs_upd[key][key_add] = 0
                    self.dif_dict[key][key_add] = 0

    def deliver_blood(self):

        pass

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
