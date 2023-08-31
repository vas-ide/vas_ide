




def popular_words(text: str, words: list) -> dict:
    upd_text = text.replace('\n', ' ').lower().split(' ')
    rezult_dict = dict.fromkeys(words, 0)
    for i in upd_text:
        if i in words:
            rezult_dict[i] += 1
    print(rezult_dict)
    return rezult_dict




popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
)

#{"i": 4, "was": 3, "three": 0, "near": 0}

