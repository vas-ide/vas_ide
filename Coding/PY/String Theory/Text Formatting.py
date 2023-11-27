def text_formatting(text: str, width: int, style: str) -> str:
    text_upd = ""
    string_upd = ""
    counter = width
    text_lst = text.split(' ')
    simbol_dict = {"l": "<", "c": "^", "r": ">", "j": ""}
    for item in text_lst:
        len_add = len(string_upd.split(" "))
        if len(item) + len_add <= counter:
            string_upd += f"{item} "
            counter -= len(item)
        else:
            print(len(string_upd))
            text_upd += "\n"
            text_upd += f"{string_upd:{simbol_dict[style]}{width}}"
            string_upd = ""
            counter = width
            string_upd += f"{item} "
            counter -= len(item)
    text_upd += f"\n{string_upd:{simbol_dict[style]}{width}}"
    print(f"{text_upd:<{width}}")
    return f"{text_upd:<{width}}"



text_formatting(
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
    38,
    "c",
)

# def test_func():
#     assert (
#         text_formatting(
#             "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#             38,
#             "l",
#         )
#         == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
#     )
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         30,
#         "c",
#     )
#     == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
# )
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         50,
#         "r",
#     )
#     == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
# )
# assert (
#     text_formatting(
#         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#         45,
#         "j",
#     )
#     == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
# )
