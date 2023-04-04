from utils import sum, subtract, multiply, divide

print('Приветствуем вас в калькуляторе Python')
q1 = float(input('Введите число 1: '))
q2 = float(input('Введите число 2: '))

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
print(f'Результат {t} = {r}')