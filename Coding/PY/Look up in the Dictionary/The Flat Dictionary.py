


# def flatten(dictionary: dict[str, str | dict], new_list=None) -> dict[str, str]:
#     if not new_list: new_list = []
#
#     for key, value in dictionary.items():
#         new_list.append(key)
#
#         if type(value) == dict and len(value) > 0:
#             flatten(value, new_list)
#         else:
#             new_list.append('*****')
#             new_list.append(value)
#
#     print(new_list)
def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    new_string = ''
    new_dict = {}
    max_len = len(dictionary)
    def annaliz(data, new_string):
        for key, value in data.items():
            if len(data) == max_len and len(data) > 1:
                new_string = ''

            if type(value) == dict:
                new_string += f'/{key}'

                if len(value) < 1:
                    new_dict[f'{new_string[1:]}'] = f""
                else:
                    annaliz(value, new_string)
            elif type(value) != dict:
                if len(new_string) > 1:
                    new_dict[f'{new_string[1:]}/{key}'] = value
                else:
                    new_dict[f'{key}'] = value
        return new_dict
    annaliz(dictionary, new_string)
    print(new_dict)
    return new_dict




flatten({"key": "value"})
# {"key": "value"}
flatten({"key": {"deeper": {"more": {"enough": "value"}}}})
# {
#     "key/deeper/more/enough": "value"
# }
flatten({"empty": {}})
# {"empty": ""}
flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
)
# {
#     "name/first": "One",
#     "name/last": "Drone",
#     "job": "scout",
#     "recent": "",
#     "additional/place/zone": "1",
#     "additional/place/cell": "2",
# }



# def func_too(number):
#     if number > 0:
#         print(number-1)
#         return func_too(number-1)
# func_too(15)



flatten({'name': {'first': 'Second', 'last': 'Drone', 'nick': {}}, 'job': {'1': 'scout', '2': 'worker', '3': 'writer', '4': 'reader', '5': 'learner'}, 'recent': {'places': {'earth': {'Louvre': '2015', 'NY': '2017', 'NP': ''}}, 'times': {'XX': {'1964': 'Yes'}, 'XXI': {'2064': 'Nope'}}}})
# {
#     'job/1': 'scout',
#     'recent/places/earth/NY': '2017',
#     'job/3': 'writer',
#     'job/2': 'worker',
#     'job/5': 'learner',
#     'job/4': 'reader',
#     'recent/places/earth/NP': '',
#     'recent/places/earth/Louvre': '2015',
#     'recent/times/XX/1964': 'Yes',
#     'recent/times/XXI/2064': 'Nope',
#     'name/first': 'Second',
#     'name/last': 'Drone',
#     'name/nick': ''
# }