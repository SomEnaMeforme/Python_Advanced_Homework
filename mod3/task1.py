import unittest
from mod2.task4 import app
from freezegun import freeze_time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def get_correct_weekday_wishes(self, correct_weekday_wishes) -> bool:
        response = self.app.get(self.base_url + 'Alex')
        response_text = response.data.decode()
        return correct_weekday_wishes in response_text

    @freeze_time('2023-03-06')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошего понедельника'))

    @freeze_time('2023-03-07')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошего вторника'))

    @freeze_time('2023-03-08')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошей среды'))

    @freeze_time('2023-03-09')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошего четверга'))

    @freeze_time('2023-03-10')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошей пятницы'))

    @freeze_time('2023-03-11')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошей субботы'))

    @freeze_time('2023-03-12')
    def test_get_correct_weekday_wishes(self):
        self.assertTrue(self.get_correct_weekday_wishes('Хорошего воскресенья'))

    def test_can_get_correct_username(self):
        username = 'Alex'
        response = self.app.get(self.base_url + 'Alex')
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_username_with_wishes(self):
        username = 'Хорошего воскресенья'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)


if __name__ == '__main__':
    unittest.main()
