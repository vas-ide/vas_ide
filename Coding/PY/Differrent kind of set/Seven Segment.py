class Display:

    def __init__(self, available, broken):
        self.available = available
        self.broken = broken
        self.analiz_left = []
        self.analiz_right = []
        self.left_digits = []
        self.right_digits = []
        self.digits_dict = {"bc": 1, "abdeg": 2, "abcdg": 3, "bcfg": 4, "acdfg": 5, "acdefg": 6, "abc": 7, "abcdefg": 8,
                            "abcdfg": 9, "abcdef": 0}
        self.total = 0

    def analiz(self):
        for item in self.available.union(self.broken):
            if item == item.upper():
                self.analiz_left.append(item)
            else:
                self.analiz_right.append(item)
        # for key, value in self.digits_dict.items():
        #     available_left = "".join(sorted(self.analiz_left))
        #     available_right = "".join(sorted(self.analiz_right))
        #     str_digit = ""
        #     for item in key:
        #         if item.upper() in available_left:
        #             str_digit += item
        #     if key == str_digit:
        #         self.left_digits.append(value)
        #     str_digit = ""
        #     for item in key:
        #         if item in available_right:
        #             str_digit += item
        #     if key == str_digit:
        #         self.right_digits.append(value)

    def generate(self):
        result = set()
        for item in self.left_digits:
            for item_add in self.right_digits:
                digit = int(f"{item}{item_add}")
                result.add(digit)
        print(len(result), result)
        self.total = len(result)

    def run(self):
        self.analiz()
        # self.generate()
        # return self.total


def seven_segment(lit_seg, broken_seg):
    dis = Display(lit_seg, broken_seg)
    dis.run()


seven_segment({'B', 'C', 'b', 'c'}, {'A'})
# == 2, '11, 71'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'})
# # == 6, '15, 16, 35, 36, 75, 76'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'})
# # == 20, '15...98'
seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'})
# # == 4   "0, 8, 80, 88"



# assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'

