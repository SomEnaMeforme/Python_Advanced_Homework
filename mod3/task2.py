import unittest
from mod2.task3 import decrypt


class TestCaseOneDot(unittest.TestCase):
    def test_delete_one_dot(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')


class TestCaseTwoDots(unittest.TestCase):
    def test_two_dots_after_letter(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')

    def test_two_dots_after_symbol(self):
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')


class TestCaseOneAndTwoDots(unittest.TestCase):
    def test_two_dots_after_letter_and_one_dot_before_letter(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')

    def test_three_dots_in_row(self):
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')

    def test_two_dots_after_digit_and_one_dot_before_digit(self):
        self.assertEqual(decrypt('1..2.3'), '23')

    def test_multiple_double_dots_and_one_dot(self):
        self.assertEqual(decrypt('абр......a.'), 'a')


class TestCaseEmptyMessage(unittest.TestCase):
    def test_many_dots_and_one_symbol(self):
        self.assertEqual(decrypt('1.......................'), '')

    def test_one_dot_without_symbols(self):
        self.assertEqual(decrypt('.'), '')

    def test_delete_all_symbols_with_double_dots(self):
        self.assertEqual(decrypt('абра........'), '')


if __name__ == '__main__':
    unittest.main()
