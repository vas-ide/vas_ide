
def deep_count(a):
    class ArrayDeepCount:

        def __init__(self):
            self.counter = 0

        def deep_count_add(self, a):
            for i in a:
                self.counter += 1
                if type(i) == list:
                    self.deep_count_add(i)

        def answer(self):
            print(self.counter)
            return self.counter

    ans = ArrayDeepCount()
    ans.deep_count_add(a)
    return ans.answer()




deep_count([])                          #0
deep_count([1, 2, 3])                   #3
deep_count(["x", "y", ["z"]])           #4
deep_count([1, 2, [3, 4, [5]]])         #7
deep_count([[[[[[[[[]]]]]]]]])          #8



