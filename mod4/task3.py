import unittest
import json
from task1 import app
from flask import Flask
from urllib.parse import unquote_plus


class TestRegistration(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.tmp_data = {'email': 'example@mail.ru',
                         'name': 'Bob',
                         'phone': 9078113455,
                         'index': 605437,
                         'address': 'Bobrovskaya 8',
                         'comment': '605437'
                         }

    def is_correct_field(self, field_name: str):
        response = self.app.post(self.base_url, data={field_name: self.tmp_data[field_name]})
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        return not(field_name in lst_errors)

    def test_correct_email(self):
        self.assertTrue(self.is_correct_field('email'))

    def test_wrong_email_format1(self):
        self.tmp_data['email'] = 'examplemail.ru'
        response = self.app.post(self.base_url, data=self.tmp_data)
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        self.assertEqual("Почта не соответствует формату",  lst_errors['email'][0])

    def test_wrong_email_format2(self):
        self.tmp_data['email'] = 'example@emailru'
        response = self.app.post(self.base_url, data=self.tmp_data)
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        self.assertEqual("Почта не соответствует формату",  lst_errors['email'][0])


    def test_wrong_email_type(self):
        self.tmp_data['email'] = 456
        response = self.app.post(self.base_url, data=self.tmp_data)
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        self.assertTrue( 'email' in lst_errors)

    def field_is_empty(self, field_name: str):
        self.tmp_data[field_name] = None
        response = self.app.post(self.base_url, data=self.tmp_data)
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        return "Поле является обязательным" == lst_errors[field_name][0]

    def test_email_is_empty(self):
        self.assertTrue(self.field_is_empty('email'))

    def test_phone_is_empty(self):
        self.assertTrue(self.field_is_empty('phone'))

    def test_index_is_empty(self):
        self.assertTrue(self.field_is_empty('index'))

    def test_name_is_empty(self):
        self.assertTrue(self.field_is_empty('name'))

    def test_address_is_empty(self):
        self.assertTrue(self.field_is_empty('address'))

    def test_correct_name(self):
        self.assertTrue(self.is_correct_field('name'))

    def test_wrong_name_type(self):
        self.tmp_data['name'] = False
        self.assertFalse(self.is_correct_field('name'))

    def test_correct_phone(self):
        self.assertTrue(self.is_correct_field('phone'))

    def test_wrong_phone_length(self):
        self.tmp_data['phone'] = 811905534
        response = self.app.post(self.base_url, data=self.tmp_data)
        data = response.get_data(as_text=True)
        lst_errors = json.loads(unquote_plus(data))
        self.assertTrue('phone' in lst_errors)

    def test_correct_index(self):
        self.assertTrue(self.is_correct_field('index'))

    def test_wrong_index_type(self):
        self.tmp_data['index'] = '98'
        self.assertFalse(self.is_correct_field('index'))

    def test_correct_address(self):
        self.assertTrue(self.is_correct_field('address'))

    def test_wrong_address_type(self):
        self.tmp_data['address'] = 98
        self.assertFalse(self.is_correct_field('address'))

    def test_correct_comment(self):
        self.assertTrue(self.is_correct_field('comment'))


if __name__ == '__main__':
    unittest.main()
