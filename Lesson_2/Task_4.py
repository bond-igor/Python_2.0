# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import re
import math
import fractions

# запрашиваем числитель и знаменатель дроби используя разделитель /
num_1, denom_1 = map(int, re.split("/", input('Введите первую дробь вида a/b: ')))
num_2, denom_2 = map(int, re.split("/", input('Введите вторая дробь вида a/b: ')))

# находим наименьшее общее кратное
nok = int((denom_1 * denom_2) / math.gcd(denom_1, denom_2))
#вычисляем числитель суммы дробей
sum_num = int(num_1 * (nok / denom_1) + num_2 * (nok / denom_2))
print(f'Сумма дробей = {sum_num}/{nok}')

#вычисляем произведение дробей

prod_num = num_1 * num_2
prod_denom = denom_1 * denom_2
print(f'Произведение дробей = {prod_num}/{prod_denom}')

# проверяем результат через встроеный метод

fract_1 = fractions.Fraction(num_1, denom_1)
fract_2 = fractions.Fraction(num_2, denom_2)
print(f'Проверка через встроеный метод: \n'
      f'Сумма дробей = {fract_1 + fract_2} \nПроизведение дробей = {fract_1 * fract_2}')
