# Sample tests


class TestSampleClass:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value != 1

    def sum_one(self, x):
        return x + 1

    def test_answer(self):
        assert self.sum_one(4) == 5
