import unittest
from task4_code_from_task import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Alex', 2000, 'Bobrovskaya 8')

    def test_init_name(self):
        self.assertEqual(self.person.name, 'Alex')

    def test_init_year_of_birth(self):
        self.assertEqual(self.person.yob, 2000)

    def test_get_name_work(self):
        self.assertEqual(self.person.get_name(), 'Alex')

    def test_get_age_work(self):
        self.assertEqual(self.person.get_age(), 23)

    def test_set_name_work(self):
        self.person.set_name('Dasha')
        self.assertEqual(self.person.name, 'Dasha')

    def test_get_address_work(self):
        self.assertEqual(self.person.get_address(), 'Bobrovskaya 8')

    def test_set_address_work(self):
        self.person.set_address('Morskaya 11')
        self.assertEqual(self.person.address, 'Morskaya 11')

    def test_is_homeless_work(self):
        person = Person('name', 2011)
        self.assertEqual(person.is_homeless(), True)

if __name__ == '__main__':
    unittest.main()
