import sys
import unittest
from task4 import RedirectOutput


class RedirectOutputTest(unittest.TestCase):
    def test_correct_work_with_two_files(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with RedirectOutput(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt', 'r') as out_file:
            self.assertEqual('Hello stdout.txt\n', out_file.read())
        with open('stderr.txt', 'r') as error_file:
                self.assertTrue('Exception: Hello stderr.txt' in error_file.read())

    def test_one_argument(self):
        print('Hello stdout')
        stdout_file = open('stdout.txt', 'w')
        with RedirectOutput(stdout=stdout_file):
            print('Hello stdout.txt')
        with open('stdout.txt', 'r') as out_file:
            self.assertEqual('Hello stdout.txt\n', out_file.read())

    def test_one_arg_stderr(self):
        stderr_file = open('stderr.txt', 'w')
        with RedirectOutput(stderr=stderr_file):
            raise Exception('Hello stderr.txt')
        with open('stderr.txt', 'r') as error_file:
            self.assertTrue('Exception: Hello stderr.txt' in error_file.read())


if __name__ == '__main__':
    unittest.main()
