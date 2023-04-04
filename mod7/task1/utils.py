import logging
from mod7.task2_logger_config import logger_config


logger = logging.getLogger('CalculationLoggerUtils')
logger_config('CalculationLoggerUtils')

def sum(a: float, b: float):
    logger.debug(f'Start sum {a} and {b}')
    return a + b


def subtract(a: float, b: float):
    logger.debug(f'Start subtract {a} and {b}')
    if b < 0:
        logger.warning('Maybe you want to use method for subtract')
    return a - b


def divide(a: float, b: float):
    logger.debug(f'Start divide {a} and {b}')
    if b == 0:
        logger.error('Zero Division Error')
        return None
    return a / b


def multiply(a: float, b: float):
    logger.debug(f'Start multiply {a} and {b}')
    return a * b


