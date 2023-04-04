import os


def is_strong_password(password: str)-> bool:
    return StrongPassword(password).is_strong_password()


class StrongPassword:
    words = []

    def __init__(self, password):
        self.password = password.lower()

    @staticmethod
    def preprocessing():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        words_file = os.path.join(base_dir, 'words.txt')
        with open(words_file, 'r') as words:
            prev_word: str = ''
            word_numb: int = 1
            for i_word in words.readlines():
                i_word = i_word[:-1].lower() #убирает знак переноса строки
                if len(i_word) <= 4 or (word_numb > 1 and prev_word in i_word):
                    continue
                else:
                    prev_word = i_word
                    StrongPassword.words.append(i_word)
                    word_numb += 1

    def is_strong_password(self) -> bool:
        if len(StrongPassword.words) == 0:
            StrongPassword.preprocessing()
        pas_len = len(self.password)
        for word in StrongPassword.words:
            if len(word) > pas_len:
                continue
            if word in self.password:
                return False
        return True


