class Tiket():
    def __init__(self, routes, departure, destination):
        self.counter = 0
        self.max_cost_lst = []
        self.cost = None
        self.routes_init = None
        self.routes = routes
        self.start_charter = None
        self.departure_init = None
        self.destination_init = None
        self.mark = True
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

    def charter_flights(self):
        for item_init in self.routes_init:
            if item_init[0] == self.departure or item_init[1] == self.departure:
                self.start_charter = item_init
                self.routes_init.remove(item_init)
                self.mark = True
                self.cost = 0
                self.cost += item_init[2]
                if self.departure == item_init[0]:
                    self.departure_init = item_init[1]
                elif self.departure == item_init[1]:
                    self.departure_init = item_init[0]
                print(self.routes_init)
                while self.mark == True:
                    self.counter += 1
                    if self.counter > 20:
                        self.mark = False
                    #     self.max_cost_lst.append(0)
                    for item in self.routes:
                        if item[0] == self.departure_init or item[1] == self.departure_init:
                            self.cost += item[2]
                            if item[0] == self.destination or item[1] == self.destination:
                                self.max_cost_lst.append(self.cost)
                                self.cost -= item[2]
                                self.routes.remove(item)
                            if self.departure_init == item[0]:
                                self.departure_init = item[1]
                            elif self.departure_init == item[1]:
                                self.departure_init = item[0]

    def min_coast(self):
        if len(self.max_cost_lst) < 1:
            self.max_cost_lst.append(0)
        self.cost = min(self.max_cost_lst)

    def run(self):
        self.direct_flight()
        self.charter_flights()
        self.min_coast()
        self.printer()

    def printer(self):
        print(self.max_cost_lst)
        if len(self.direct_flight_lst) > 0:
            print(self.direct_flight_lst, f"Direct cost is {self.direct_flight_lst[2]}")
        else:
            print(self.direct_flight_lst, f"We don't have direct flight")
        print(f"Min coast is {self.cost}")


def cheapest_flight(costs: list, a: str, b: str) -> int:
    tic = Tiket(routes=costs, departure=a, destination=b)
    tic.run()
    return tic.cost


# cheapest_flight([['A', 'B', 10], ['A', 'C', 20], ['B', 'D', 15], ['C', 'D', 5], ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A', 'F') == 40

# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
# cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
# cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25


# assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70)
# assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70)
# assert (cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D",
#                         "C", ) == 60)
# assert (cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0)
assert (cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D") == 25)
