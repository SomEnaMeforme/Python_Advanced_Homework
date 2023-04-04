from utils import sum, subtract, multiply, divide
import logging
from mod7.task2_logger_config import logger_config


logger = logging.getLogger('CalculationLoggerApps')
logger_config('CalculationLoggerApps')


logger.warning('Not ASCII symbols: ÎŒØ∏‡°⁄·°€йцукен')
logger.info('Приветствуем вас в калькуляторе Python')
logger.info('Welcome to Calculator Python')
q1 = float(input('Введите число 1: '))
q2 = float(input('Введите число 2: '))


logger.debug('Get command from user')
v = int(input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))
t = ''
r = 0
if v == 1:
    r = sum(q1, q2)
    p = 'сложения'
    t = p
if v == 2:
    r = subtract(q1, q2)
    l = 'вычитания'
    t = l
if v == 3:
    r = divide(q1, q2)
    m = 'деления'
    t = m
if v == 4:
    r = multiply(q1, q2)
    n = 'умножения'
    t = n
logger.info(f'Результат {t} = {r}')
