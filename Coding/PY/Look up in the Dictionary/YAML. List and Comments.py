import random


class YAML():
    def __init__(self, string):
        self.string = string
        self.lst_upd = []
        self.info_dict = {}

    def analiz(self):
        lst = self.string.split('\n')
        counter = 0
        for i in lst:
            if ":" in i:
                counter += 1
        if counter < 1:
            self.list_yaml(lst)
        else:
            self.dict_yaml(lst)

    def dict_yaml(self, lst):
        for i in lst:
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
                    self.info_dict[lst_analiz[0]] = int(lst_analiz[1])
                except:
                    if lst_analiz[1].strip() == 'true':
                        self.info_dict[lst_analiz[0]] = True
                    elif lst_analiz[1].strip() == 'false':
                        self.info_dict[lst_analiz[0]] = False
                    elif lst_analiz[1] == f'Non-determinate{dice}':
                        self.info_dict[lst_analiz[0]] = None
                    else:
                        self.info_dict[lst_analiz[0]] = lst_analiz[1].strip()

    def list_yaml(self, lst):
        for i in lst:
            if ":" not in i:
                if len(i) == 1 and i == '-':
                    self.lst_upd.append(None)
                elif len(i) > 1:
                    i = i.replace('- ', '')
                    if i.count('"') == 2:
                        self.lst_upd.append(i[1:-1])
                    else:
                        new_string = ''
                        for j in i:
                            if j == '#':
                                if len(new_string) > 0:
                                    try:
                                        self.lst_upd.append(int(new_string.strip()))
                                    except:
                                        self.lst_upd.append(new_string.strip())
                                new_string = ''
                                break
                            else:
                                new_string += j
                        if len(new_string) > 0:
                            try:
                                self.lst_upd.append(int(new_string.strip()))
                            except:
                                self.lst_upd.append(new_string.strip())
                        new_string = ''


def yaml(a: str) -> list:
    yaml_test = YAML(a)
    yaml_test.analiz()
    if len(yaml_test.lst_upd) > len(yaml_test.info_dict):
        print(yaml_test.lst_upd)
        return yaml_test.lst_upd
    else:
        print(yaml_test.info_dict)
        return yaml_test.info_dict


yaml('\nname: Alex\nage: 12')
# {'name': 'Alex', 'age': 12})


yaml("name: Alex\nage: 12")
# # {"name": "Alex", "age": 12}
yaml("name: Alex Fox\nage: 12\n\nclass: 12b")
# # {
# #     "name": "Alex Fox",
# #     "age": 12,
# #     "class": "12b",
# # }
yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b')
# # {
# #     "name": "Alex Fox",
# #     "age": 12,
# #     "class": "12b",
# # }
yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b')
# # {
# #     "name": 'Alex "Fox"',
# #     "age": 12,
# #     "class": "12b",
# # }
yaml('name: "Bob Dylan"\nchildren: 6\nalive: false')
# # {
# #     "name": "Bob Dylan",
# #     "children": 6,
# #     "alive": False,
# # }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding:')
# # {
# #     "name": "Bob Dylan",
# #     "children": 6,
# #     "coding": None,
# # }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null')
# # {
# #     "name": "Bob Dylan",
# #     "children": 6,
# #     "coding": None,
# # }
yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ')
# # {
# #     "name": "Bob Dylan",
# #     "children": 6,
# #     "coding": "null",
# # }

yaml('- write some\n- "Alex Chii"\n- 89')
# ["write some", "Alex Chii", 89]
yaml('# comment\n- write some # after\n# one mor\n- "Alex Chii #sir "\n- 89 #bl')
# # ["write some", "Alex Chii #sir ", 89]
yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5")
# [1, 2, 3, 4, 5]
yaml("-\n-\n-\n- 7")
# [None, None, None, 7]
