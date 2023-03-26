import unittest
from task3_context_manager import BlockErrors


class BlockErrorsTest(unittest.TestCase):

    def test_simple_test_without_errors(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / '0'
        print('Выполнено без ошибок')

    def test_simple_test_with_error(self):
        err_types = {ZeroDivisionError}
        with self.assertRaises(TypeError):
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')

    def test_outdoor_and_indoor_unit(self):
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with self.assertRaises(TypeError):
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
        print('Внешний блок: выполнено без ошибок')

    def test_suberrors(self):
        err_types = {Exception}
        with BlockErrors(err_types):
            a = 1 / '0'
        print('Выполнено без ошибок')


if __name__ == '__main__':
    unittest.main()
