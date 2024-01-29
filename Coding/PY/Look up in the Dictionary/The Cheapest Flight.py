class Tiket():
    def __init__(self, routes, departure, destination):
        self.max_cost_lst = []
        self.charter_min_cost = None
        self.generate_rutes = {}
        self.routes_init = None
        self.routes_dict = {}
        self.routes = routes
        self.departure = departure
        self.destination = destination
        self.direct_flight_lst = []

    def direct_flight(self):
        for num, item in enumerate(self.routes):
            if item[0] == self.departure and item[1] == self.destination:
                self.routes.pop(num)
                self.direct_flight_lst = item
                self.max_cost_lst.append(self.direct_flight_lst[2])
            elif item[1] == self.departure and item[0] == self.destination:
                self.routes.pop(num)
                self.direct_flight_lst = item
                self.max_cost_lst.append(self.direct_flight_lst[2])
        self.routes_init = self.routes

    def generate_init_dict(self):
        for item in self.routes:
            self.routes_dict[f"{item[0]}{item[1]}"] = item[2]

    def generate_direction(self):
        for key, value in self.routes_dict.items():
            if self.departure in [item for item in key]:
                if key[0] != self.departure:
                    key = key[::-1]
                for key_add, value_add in self.routes_dict.items():
                    if key[-1] == key_add[0]:
                        self.generate_rutes[f"{key}{key_add[1:]}"] = value + value_add
                    if key[-1] == key_add[1]:
                        self.generate_rutes[f"{key}{key_add[::-1][1]}"] = value + value_add
        self.clear_dict()

    #
    def combinete_charter(self):
        if len(self.generate_rutes) > 0:
            combinete_dict = {}
            for key, value in self.generate_rutes.items():
                for key_add, value_add in self.routes_dict.items():
                    if key[-1] == self.destination:
                        combinete_dict[key] = value
                    else:
                        if key[-1] == key_add[0] and key_add[1] not in [item for item in key]:
                            combinete_dict[f"{key}{key_add[1:]}"] = value + value_add
                        if key[-1] == key_add[1] and key_add[0] not in [item for item in key]:
                            combinete_dict[f"{key}{key_add[::-1][1]}"] = value + value_add
                if combinete_dict == self.generate_rutes:
                    return
            self.generate_rutes = combinete_dict
            self.clear_dict()
            self.combinete_charter()

    def clear_dict(self):
        dict_upd = {}
        for key, value in self.generate_rutes.items():
            if key[0] == self.departure:
                if key[-1] != self.departure:
                    dict_upd[key] = value
                elif key[-1] == self.destination:
                    dict_upd[key] = value
        self.generate_rutes = dict_upd

    def min_coast(self):
        if len(self.generate_rutes) < 1:
            self.max_cost_lst.append(0)
        [self.max_cost_lst.append(value) for key, value in self.generate_rutes.items() if
         key[0] == self.departure and key[-1] == self.destination]
        self.charter_min_cost = min(self.max_cost_lst)


    def run(self):
        self.direct_flight()
        self.generate_init_dict()
        self.generate_direction()
        self.combinete_charter()
        self.min_coast()
        self.printer()

    def printer(self):
        print(self.charter_min_cost)
        # print(self.max_cost_lst)
        # print(self.generate_rutes)
        # if len(self.direct_flight_lst) > 0:
        #     print(self.direct_flight_lst, f"Direct cost is {self.direct_flight_lst[2]}")
        # else:
        #     print(self.direct_flight_lst, f"We don't have direct flight")




def cheapest_flight(costs: list, a: str, b: str) -> int:
    tic = Tiket(routes=costs, departure=a, destination=b)
    tic.run()
    return tic.charter_min_cost


cheapest_flight(
    [['A', 'B', 10], ['A', 'C', 20], ['B', 'D', 15], ['C', 'D', 5], ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A',
    'F') == 40
#
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
# cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
# cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25

assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70)
assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70)
assert (cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D",
                        "C", ) == 60)
assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0)
assert (cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D") == 25)
