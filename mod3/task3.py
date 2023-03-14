import unittest
from mod2.task7 import app, Finance


class FinanceTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/'
        Finance.storage = {
            2020: {4: 1002, 12: 10, 3: 132, 1: 7856, 9: 99},
            2023: {11: 112, 2: 376, 6: 12, 12: 74, 9: 99},
            1999: {1: 45, 7: 8, 4: 4}
        }

    def test_method_add_work_correct(self):
        self.app.get(self.base_url + 'add/19990105/1')
        self.assertEqual(Finance.storage[1999][1], 46)

    def test_method_calculate_with_year_work_correct(self):
        response = self.app.get(self.base_url + 'calculate/1999')
        response_text = response.data.decode()
        self.assertEqual(response_text, '57')

    def test_method_calculate_with_year_and_month_work_correct(self):
        response = self.app.get(self.base_url + 'calculate/2023/11')
        response_text = response.data.decode()
        self.assertEqual(response_text, '112')

    def test_add_with_wrong_date_format(self):
        with self.assertRaises(ValueError):
            self.app.get(self.base_url + 'add/01-12-2000/1')

    def test_calculate_with_wrong_month(self):
        response = self.app.get(self.base_url + 'calculate/2023/13')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'Некорректные значения входных данных')

    def test_add_with_new_year(self):
        self.app.get(self.base_url + 'add/19970105/1')
        self.assertEqual(Finance.storage[1997][1], 1)

    def test_calculate_with_empty_year(self):
        response = self.app.get(self.base_url + 'calculate/')
        self.assertEqual(response.status_code, 404)


class EmptyStorage(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/'

    def test_calculate_year_with_empty_storage(self):
        response = self.app.get(self.base_url + 'calculate/1997')
        response_text = response.data.decode()
        self.assertEqual(response_text, '0')

    def test_calculate_year_and_month_with_empty_storage(self):
        response = self.app.get(self.base_url + 'calculate/1997/1')
        response_text = response.data.decode()
        self.assertEqual(response_text, '0')


if __name__ == '__main__':
    unittest.main()
