import re

def text_formatting(text: str, width: int, style: str) -> str:
    text_upd = ""
    string_lst = []
    string_upd = ""
    counter = width
    text_lst = text.split(' ')
    simbol_dict = {"l": "<", "c": "^", "r": ">", "j": "", "t": "\n"}
    for item in text_lst:
        len_add = len(string_upd.split(" "))
        if len(item) + len_add -1 <= counter:
            string_upd += f"{item} "
            counter -= len(item)
        else:
            string_upd = f"{ string_upd:{simbol_dict[style]}{width}}"
            string_upd = re.sub(r"\s+$", "", string_upd)
            text_upd += f"{string_upd}\n"
            string_upd = ""
            counter = width
            string_upd += f"{item} "
            counter -= len(item)

    string_upd = f"{string_upd:{simbol_dict[style]}{width}}"
    string_upd = re.sub(r"\s+$", "", string_upd)
    text_upd += f"{string_upd}"
    print(text_upd)
    return text_upd


    #     else:
    #         string_upd = f"{string_upd:{simbol_dict[style]}{width}}"
    #         text_upd += f"{string_upd}\n"
    #         string_upd = ""
    #         counter = width
    #         string_upd += f"{item} "
    #         counter -= len(item)
    #
    # string_upd = f"{string_upd:{simbol_dict[style]}{width}}"
    # text_upd += f"{string_upd}"
    # print(f"{text_upd:<{width}}")
    # return f"{text_upd:<{width}}"






# text_formatting(
#     "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#     38,
#     "l",
# )
# text_formatting(
#     "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
#     30,
#     "c",
# )

class TestAdd:

    def test_text(self):
        pass
        # assert (
        #     text_formatting(
        #         "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        #         38,
        #         "l",
        #     )
        #     == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
        # )
        assert (
            text_formatting(
                "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
                30,
                "c",
            )
            == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
        )
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
