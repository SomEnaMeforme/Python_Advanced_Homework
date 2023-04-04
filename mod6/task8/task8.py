import re
import os

class MyT9:
    symbol_for_numb = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    @staticmethod
    def my_t9(word: str):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        words_file = os.path.join(base_dir, 'task2/words.txt')
        match = ''
        for numb in word:
            if numb == '1' or not(numb.isdigit()):
                return ''
            number = int(numb)
            match += f'[{MyT9.symbol_for_numb[number]}]'
        with open(words_file, 'r') as words:
            words_str = words.read()
        return set(re.findall(match, words_str))


if __name__ == '__main__':
    for word in MyT9.my_t9('22736368'):
        print(word)

