def best_stock(data: dict[str, float]) -> str:
    max_value = max(data.values())
    rezult = {k:v for k,v in data.items() if v==max_value}
    print(list(rezult)[0])
    return list(rezult)[0]





best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2})
#"ATX"
best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9})
#"TASI"

