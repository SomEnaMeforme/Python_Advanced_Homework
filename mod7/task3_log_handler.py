import logging
import os

class LogHandlerForCalculator(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record: logging.LogRecord):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        logs_file = os.path.join(base_dir, f'task1/calc_{record.levelname}.log')
        if self.filter(record):
            with open(logs_file, 'a') as logs:
                logs.write(self.format(record))
