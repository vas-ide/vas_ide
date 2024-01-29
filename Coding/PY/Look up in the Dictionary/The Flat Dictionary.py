
def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    pass
    dict_upd = {}

    key_str = ""
    val_str = ""

    for key, value in dictionary.items():
        if type(key) == str and type(value) == str:
            if len(key_str) < 1:
                key_str += f"{key}"
                val_str = value
                dict_upd[key_str] = val_str
            else:
                key_str += f"{val_str}"
                key_str += f"/{key}"
                val_str = value
                dict_upd[key_str] = val_str
        elif type(value) == dict and len(value) == 1:


            if len(key_str) < 1:
                key_str += f"{key}"
                val_str = value
            else:
                key_str += f"{val_str}"
                key_str += f"/{key}"
                val_str = value
            flatten(dictionary)
    print(dict_upd)


flatten({"key": "value"})
# {"key": "value"}
flatten({"key": {"deeper": {"more": {"enough": "value"}}}})
# {
#     "key/deeper/more/enough": "value"
# }
# flatten({"empty": {}})
# {"empty": ""}
# flatten(
#     {
#         "name": {"first": "One", "last": "Drone"},
#         "job": "scout",
#         "recent": {},
#         "additional": {"place": {"zone": "1", "cell": "2"}},
#     }
# )
# {
#     "name/first": "One",
#     "name/last": "Drone",
#     "job": "scout",
#     "recent": "",
#     "additional/place/zone": "1",
#     "additional/place/cell": "2",
# }


# flatten(
#     {'name': {'first': 'Second', 'last': 'Drone', 'nick': {}},
#      'job': {'1': 'scout', '2': 'worker', '3': 'writer', '4': 'reader', '5': 'learner'},
#      'recent': {'places': {'earth': {'Louvre': '2015', 'NY': '2017', 'NP': ''}},
#                 'times': {'XX': {'1964': 'Yes'}, 'XXI': {'2064': 'Nope'}}}}
# )
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




# assert flatten({"key": "value"}) == {"key": "value"}
# assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
#     "key/deeper/more/enough": "value"
# }
# assert flatten({"empty": {}}) == {"empty": ""}
# assert flatten(
#     {
#         "name": {"first": "One", "last": "Drone"},
#         "job": "scout",
#         "recent": {},
#         "additional": {"place": {"zone": "1", "cell": "2"}},
#     }
# ) == {
#     "name/first": "One",
#     "name/last": "Drone",
#     "job": "scout",
#     "recent": "",
#     "additional/place/zone": "1",
#     "additional/place/cell": "2",
# }


































