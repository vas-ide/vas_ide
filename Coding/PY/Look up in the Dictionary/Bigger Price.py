
def bigger_price(limit:int, data: list[dict]):

    max_list = []
    [max_list.append(i['price']) for i in data]
    max_list_upd = sorted(max_list,reverse=1)[:limit]
    rezult_list = []

    for i in max_list_upd:
        for j in data:
            if i == j['price']:
                rezult_list.append(j)

    print(rezult_list)
    return rezult_list




data_inf = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1},
]
bigger_price(1, data_inf)
bigger_price(3, data_inf)
bigger_price(2, data_inf)






