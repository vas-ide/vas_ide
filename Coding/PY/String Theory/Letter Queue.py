from typing import List


def letter_queue(commands: List[str]) -> str:
    answer_str = f""
    answer_lst = []
    if len(commands) < 1:
        return answer_str
    for i in commands:
        if i == "POP":
            if len(answer_lst) < 1:
                pass
            else:
                answer_lst.pop(0)
        else:
            answer_lst.append(i[-1])
    answer_str = "".join(answer_lst)
    return answer_str


    # for i in commands:
    #     if len(i) == 3:
    #         return None


class TestAdd:

    def test_standart(self):
        assert (
            letter_queue(
                ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
            )
            == "DOT"
        )
        assert letter_queue(["POP", "POP"]) == ""
        assert letter_queue(["PUSH H", "PUSH I"]) == "HI"
        assert letter_queue([]) == ""

    def test_add(self):
        assert (
                letter_queue(
                    ["PUSH Y", "POP", "POP", "PUSH Z", "PUSH V", "PUSH A", "POP", "PUSH S"]
                )
                == "VAS"
        )

