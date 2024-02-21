class Display:

    def __init__(self, available, broken):
        self.available = available
        self.broken = broken
        self.init_analiz_left = []
        self.init_analiz_right = []
        self.analiz_left = []
        self.analiz_right = []
        self.left_digits = []
        self.right_digits = []
        self.data = []
        self.digits_dict = {"bc": 1, "abdeg": 2, "abcdg": 3, "bcfg": 4, "acdfg": 5, "acdefg": 6, "abc": 7, "abcdefg": 8,
                            "abcdfg": 9, "abcdef": 0}
        self.result = set()

    def init_analiz(self):
        [self.init_analiz_left.append(item) for item in self.available if item.upper() == item]
        [self.init_analiz_right.append(item) for item in self.available if item.lower() == item]
        if type(self.available) is set:
            self.data = self.available.union(self.broken)
        else:
            [self.data.append(item) for item in self.broken]

        for item in self.data:
            if item == item.upper():
                self.analiz_left.append(item)
            else:
                self.analiz_right.append(item)

    def analiz(self):

        for key, value in self.digits_dict.items():
            available_left = "".join(sorted(self.analiz_left))
            available_right = "".join(sorted(self.analiz_right))
            str_digit = ""
            for item in key:
                if item.upper() in list(available_left):
                    str_digit += item
            if key == str_digit and len(self.available) < 1:
                self.left_digits.append(value)
            elif key == str_digit and len(self.available) > 1:
                counter = 0
                for item in self.init_analiz_left:
                    if item.lower() in list(key):
                        counter += 1
                    if counter == len(self.init_analiz_left):
                        self.left_digits.append(value)
            str_digit = ""
            for item in key:
                if item in list(available_right):
                    str_digit += item
            if key == str_digit and len(self.available) < 1:
                self.right_digits.append(value)
            elif key == str_digit and len(self.available) > 1:
                counter = 0
                for item in self.init_analiz_right:
                    if item in list(key):
                        counter += 1
                    if counter == len(self.init_analiz_right):
                        self.right_digits.append(value)

    def generate(self):

        for item in self.left_digits:
            for item_add in self.right_digits:
                digit = int(f"{item}{item_add}")
                self.result.add(digit)

    def run(self):
        self.init_analiz()
        self.analiz()
        self.generate()
        print(len(self.result), self.result)


def seven_segment(lit_seg, broken_seg):
    dis = Display(lit_seg, broken_seg)
    dis.run()
    return len(dis.result)


seven_segment({'B', 'C', 'b', 'c'}, {'A'})
# == 2, '11, 71'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'})
# # == 6, '15, 16, 35, 36, 75, 76'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'})
# # == 20, '15...98'
seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'})
# # == 4   "0, 8, 80, 88"
seven_segment([], ["A", "B", "C", "D", "E", "F", "G", "a", "b", "c", "d", "e", "f", "g"])

# assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
