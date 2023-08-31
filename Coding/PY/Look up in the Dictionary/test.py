def cheapest_flight(costs: list, a: str, b: str) -> int:
    delay_airport = ''
    way = []
    direct = []
    for i in costs:
        if a == i[0] and b == i[1] or a == i[1] and b == i[0]:
            direct.append(i[2])
        elif a == i[0]:
            delay_airport = i[1]
        elif a == i[1]:
            delay_airport = i[0]
        for j in costs:
            if i[0] == a and i[1] == delay_airport and j[0] == b and j[1] == delay_airport or \
                    i[0] == a and i[1] == delay_airport and j[1] == b and j[0] == delay_airport or \
                    i[1] == a and i[0] == delay_airport and j[1] == b and j[0] == delay_airport or \
                    i[1] == a and i[0] == delay_airport and j[0] == b and j[1] == delay_airport:
                way.append(i[2] + j[2])

    if len(way) < 1 and len(direct) < 1:
        print(f"{0}")
        return 0
    elif len(direct) == 0 and len(way) > 0:
        print(f"{min(way)}")
        return min(way)
    elif min(way) < direct[0]:
        print(f"{min(way)}")
        return min(way)




cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25
