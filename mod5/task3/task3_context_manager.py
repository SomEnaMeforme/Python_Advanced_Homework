class BlockErrors():
    def __init__(self, error_types):
        self.error_types = error_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        for type in self.error_types:
            if exc_type == None or exc_type == type or issubclass(exc_type, type):
                return True
        return False
