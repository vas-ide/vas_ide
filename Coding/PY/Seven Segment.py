class Display:

    def __init__(self):
        pass

    def analiz(self):
        pass


def seven_segment(lit_seg, broken_seg):
    return 0


seven_segment({'B', 'C', 'b', 'c'}, {'A'})
# == 2, '11, 71'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'})
# == 6, '15, 16, 35, 36, 75, 76'
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'})
# == 20, '15...98'


# assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
# assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
