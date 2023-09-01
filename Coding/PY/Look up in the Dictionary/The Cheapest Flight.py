def cheapest_flight(costs: list, a: str, b: str) -> int:
    total_cost = 0
    dep = ''
    tranzit = ''
    arr = ''
    for i in costs:
        if a in i and b not in i:


            for j in costs:
                for z in j:
                    pass





    #     elif b in i and a not in i:
    #         total_cost += i[2]
    # print(total_cost)










cheapest_flight([['A', 'B', 10], ['A', 'C', 20], ['B', 'D', 15], ['C', 'D', 5], ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A', 'F') == 40


cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")  # == 70
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")  # == 70
cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70], ], "D", "C")  # == 60
cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")  # == 0
cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")  # == 25





# def cheapest_flight(costs: list, a: str, b: str) -> int:
#     delay_airport = ''
#     way = []
#     direct = []
#     for i in costs:
#         if a == i[0] and b == i[1] or a == i[1] and b == i[0]:
#             direct.append(i[2])
#         elif a == i[0]:
#             delay_airport = i[1]
#         elif a == i[1]:
#             delay_airport = i[0]
#         for j in costs:
#             if i[0] == a and i[1] == delay_airport and j[0] == b and j[1] == delay_airport or \
#                     i[0] == a and i[1] == delay_airport and j[1] == b and j[0] == delay_airport or \
#                     i[1] == a and i[0] == delay_airport and j[1] == b and j[0] == delay_airport or \
#                     i[1] == a and i[0] == delay_airport and j[0] == b and j[1] == delay_airport:
#                 way.append(i[2] + j[2])
#
#     if len(way) < 1 and len(direct) < 1:
#         print(f"{0}")
#         return 0
#     elif len(direct) == 0 and len(way) > 0:
#         print(f"{min(way)}")
#         return min(way)
#     elif min(way) < direct[0]:
#         print(f"{min(way)}")
#         return min(way)

# dep = ''
# arr = ''
# delay_airport = ''
# final_coast = 0
# for i in costs:
#     if i[0] == a and i[1] == b or i[0] == b and i[1] == a:
#         pass
#     elif a == i[0]:
#         if final_coast != 0:
#             final_coast = 0
#         dep = a
#         delay_airport = i[1]
#         final_coast += i[2]
#     elif a == i[1]:
#         if final_coast != 0:
#             final_coast = 0
#         dep = a
#         delay_airport = i[0]
#         final_coast += i[2]
# for i in costs:
#     if i[0] == a and i[1] == b or i[0] == b and i[1] == a:
#         pass
#     elif delay_airport == i[0] and b == i[1] or delay_airport == i[1] and b == i[0]:
#         final_coast += i[2]
#         arr = b
# if len(arr) < 1:
#     final_coast = 0



