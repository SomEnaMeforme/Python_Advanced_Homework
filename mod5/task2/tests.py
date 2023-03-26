import unittest
from task2_run_python_code import app
import json
from urllib.parse import unquote_plus

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/python_code'
        self.tmp_data = {'body': 'print("Hello world!")',
                         'max_time': 30,
                         }
    def is_correct_field(self, field_name: str):
        response = self.app.post(self.base_url, data={field_name: self.tmp_data[field_name]})
        return response.get_data(as_text=True) != 'Проверьте введённые данные'

    def test_wrong_time(self):
        self.tmp_data['max_time'] = 'пять'
        self.assertFalse(self.is_correct_field('max_time'))

    def test_wrong_body(self):
        self.tmp_data['body'] = 404
        self.assertFalse(self.is_correct_field('body'))

    def test_unsafe_code(self):
        self.tmp_data['body'] = "from subprocess import run\nrun(['./kill_the_system.sh'])"
        resp = self.app.post(self.base_url, data=self.tmp_data)
        data = resp.get_data(as_text=True)
        self.assertTrue('BlockingIOError' in data)

    def test_little_time(self):
        self.tmp_data['max_time'] = 0
        self.tmp_data['body'] = "import time\ntime.sleep(5)"
        with self.assertRaises(TimeoutError):
            self.app.post(self.base_url, data=self.tmp_data)


if __name__ == '__main__':
    unittest.main()
