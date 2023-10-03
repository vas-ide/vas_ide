class Tiket():
    def __init__(self, routes, departure, destination):
        self.max_cost = 1000000
        self.cost = 0
        self.routes_init = routes
        self.routes = routes
        self.departure_init = departure
        self.destination_init = destination
        self.departure = departure
        self.destination = destination


    def run(self):

        for i in self.routes_init:
            self.routes = self.routes_init
            self.max_cost_ticket()
            # while True:
            for j in self.routes:
                if j[0] == self.departure:
                    self.departure = j[1]
                    self.cost += j[2]
                elif j[1] == self.departure:
                    self.departure = j[0]
                    self.cost += j[2]
                self.routes.remove(j)
                self.max_cost_ticket()


    def max_cost_ticket(self):
        for i in self.routes:
            if self.departure in i and self.destination in i:
                self.routes.remove(i)
                if self.max_cost > (self.cost + i[2]):
                    self.max_cost = self.cost + i[2]

def cheapest_flight(costs: list, a: str, b: str) -> int:
    tic = Tiket(routes=costs, departure=a, destination=b)
    tic.run()
    print(tic.max_cost)


# cheapest_flight([['A', 'B', 10], ['A', 'C', 20], ['B', 'D', 15], ['C', 'D', 5], ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A', 'F') == 40


cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
# cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
# cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
# cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25

