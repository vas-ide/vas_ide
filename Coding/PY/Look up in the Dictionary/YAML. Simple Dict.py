



def yaml(a: str) -> dict:
    info_dict = {}
    print(a.split('\n'))
    for i in a.split('\n'):
        if len(i) > 0:
            i_upd = i.split(':')
            try:
                info_dict[i_upd[0]] = int(i_upd[1])
            except:
                info_dict[i_upd[0]] = i_upd[1]
    print(info_dict)
    return info_dict




yaml("name: Alex\nage: 12")
#{"name": "Alex", "age": 12}
yaml("name: Alex Fox\nage: 12\n\nclass: 12b")
# {
#     "age": 12,
#     "name": "Alex Fox",
#     "class": "12b",
# }



















