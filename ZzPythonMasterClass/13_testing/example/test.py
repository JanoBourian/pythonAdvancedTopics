import unittest
from script import run_guess


class TestGame(unittest.TestCase):

    def test_input(self):
        result = run_guess(5, 5)
        self.assertEqual(result, True)

    def test_input_wrong(self):
        result = run_guess(4, 5)
        self.assertEqual(result, False)

    def test_input_incorret(self):
        result = run_guess('11', 5)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
