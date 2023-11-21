# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX = 16

num = int(input('Введите целое число: '))
number_new = ''
check_num = num

while num:
    if num % HEX == 10:
        num_char = 'A'
    elif num % HEX == 11:
        num_char = 'B'
    elif num % HEX == 12:
        num_char = 'C'
    elif num % HEX == 13:
        num_char = 'D'
    elif num % HEX == 14:
        num_char = 'E'
    elif num % HEX == 15:
        num_char = 'F'
    else:
        num_char = str(num % HEX)
    number_new = num_char + number_new
    num //= HEX

print(f'В 16-ой системе счисления = {number_new}')
print(f'Проверка: {hex(check_num)}')

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions
import math

frac_1 = list(map(int, input('Введите первую дробь формата "a/b": ').split('/')))
frac_2 = list(map(int, input('Введите вторую дробь формата "a/b": ').split('/')))

sum_div = frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1]
sum_denom = frac_1[1] * frac_2[1]
sum_gcd = math.gcd(sum_div, sum_denom)
if sum_denom / sum_gcd != 1:
    sum_fracs = f'{int(sum_div / sum_gcd)}/{int(sum_denom / sum_gcd)}'
else:
    sum_fracs = int(sum_div / sum_gcd)

prod_div = frac_1[0] * frac_2[0]
prod_denom = frac_1[1] * frac_2[1]
prod_gcd = math.gcd(prod_div, prod_denom)
if prod_denom / prod_gcd != 1:
    prod_fracs = f'{int(prod_div / prod_gcd)}/{int(prod_denom / prod_gcd)}'
else:
    prod_fracs = int(prod_div / prod_gcd)

print(f'Сумма дробей - {sum_fracs}, Произведение дробей - {prod_fracs}')

f1 = fractions.Fraction(frac_1[0], frac_1[1])
f2 = fractions.Fraction(frac_2[0], frac_2[1])
print(f'Проверка:\nСумма дробей - {f1 + f2}, Произведение дробей - {f1 * f2}')
