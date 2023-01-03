import unittest
from main import LotteryParser


class ParseTest(unittest.TestCase):
    def test_check_parse_correct(self):
        result1 = LotteryParser("1,2,3,4,5,6").run()
        self.assertEqual(result1, [1, 2, 3, 4, 5, 6])  # add assertion here

    def test_check_wrong_input(self):
        result1 = LotteryParser("1,2,3").run()
        self.assertEqual(result1, "1,2,3")


if __name__ == '__main__':
    unittest.main()
