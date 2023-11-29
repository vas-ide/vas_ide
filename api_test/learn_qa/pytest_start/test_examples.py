





class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expect_sum = 14
        assert a + b == expect_sum, f"Sum of variables a and b is not equal to {expect_sum}"
    def test_check_math_upd(self):
        a = 11
        b = 9
        expect_sum = 20
        assert a + b == expect_sum, f"Sum of variables a and b is not equal to {expect_sum}"
