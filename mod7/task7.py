import logging

class ASCIIFilter(logging.Filter):

    def filter(self, record):
        result = 1 if record.msg.isascii() else 0
        return result
