def cheapest_flight(costs: list, a: str, b: str) -> int:
    delay_airport = ''
    final_coast = 0
    for i in costs:
        if i[0] == a and i[1] == b or i[0] == b and i[1] == a:
            pass
        elif a == i[0]:
            if final_coast != 0:
                final_coast = 0
            delay_airport = i[1]
            final_coast += i[2]
        elif a == i[1]:
            if final_coast != 0:
                final_coast = 0
            delay_airport = i[0]
            final_coast += i[2]
    for i in costs:
        if i[0] == a and i[1] == b or i[0] == b and i[1] == a:
            pass
        elif delay_airport == i[1] and b == i[0] or delay_airport == i[0] and b == i[1]:
            final_coast += i[2]

    print(final_coast)


cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25
