import random


def yaml(a: str) -> dict:
    info_dict = {}
    print(a.split('\n'))
    for i in a.split('\n'):
        # if ":" in i:
        if len(i) > 0:
            # print(i)
            dice = random.randint(0, 1000000)
            if 'null' in i and '"null"' not in i:
                lst_analiz = i.split(':')
                lst_analiz[1] = f'Non-determinate{dice}'
            elif '"' in i:
                lst_analiz = i.replace('"', '').split(':')
            else:
                lst_analiz = i.split(':')

            if '\\' in lst_analiz[1]:
                lst_analiz[1] = lst_analiz[1].replace("\\", '"')

            if len(lst_analiz[1]) < 1:
                lst_analiz[1] = f'Non-determinate{dice}'

            try:
                info_dict[lst_analiz[0]] = int(lst_analiz[1])
            except:
                if lst_analiz[1].strip() == 'true':
                    info_dict[lst_analiz[0]] = True
                elif lst_analiz[1].strip() == 'false':
                    info_dict[lst_analiz[0]] = False
                elif lst_analiz[1] == f'Non-determinate{dice}':
                    info_dict[lst_analiz[0]] = None
                else:
                    info_dict[lst_analiz[0]] = lst_analiz[1].strip()
    print(info_dict)
    return info_dict


yaml("name: Alex\nage: 12")
# {"name": "Alex", "age": 12}
yaml("name: Alex Fox\nage: 12\n\nclass: 12b")
# {
#     "name": "Alex Fox",
#     "age": 12,
#     "class": "12b",
# }
yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b')
# {
#     "name": "Alex Fox",
#     "age": 12,
#     "class": "12b",
# }
yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b')
# {
#     "name": 'Alex "Fox"',
#     "age": 12,
#     "class": "12b",
# }
yaml('name: "Bob Dylan"\nchildren: 6\nalive: false')
# {
#     "name": "Bob Dylan",
#     "children": 6,
#     "alive": False,
# }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding:')
# {
#     "name": "Bob Dylan",
#     "children": 6,
#     "coding": None,
# }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null')
# {
#     "name": "Bob Dylan",
#     "children": 6,
#     "coding": None,
# }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ')
# {
#     "name": "Bob Dylan",
#     "children": 6,
#     "coding": "null",
# }
