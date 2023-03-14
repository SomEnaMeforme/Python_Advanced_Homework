from datetime import datetime


class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = None):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self) -> int:
        return datetime.now().year - self.yob

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def set_address(self, address: str):
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        '''
        returns True if address is not set, false in other case
        '''
        return self.address is None
