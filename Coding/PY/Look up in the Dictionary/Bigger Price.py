
def select(limit:int, data: list[dict]):
    max_list = []
    for i in data:
        max_list.append([v for k,v in i.items() if k=='price'])
    couter = 0
    rezult_list = []

    while couter != limit:
        max_value = max(max_list)
        for i in data:
            print(i)
            if [v for k, v in i.items() if v == max_value]:
                rezult_list.append(i)
        max_list.remove(max_value)
        couter += 1


    print(max_list,rezult_list)









data_inf = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1},
]
select(2, data_inf)






