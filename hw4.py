# 1. Напишите функцию для транспонирования матрицы


def print_matrix(matrix: [[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()


def matrix_transposition(matrix: [[int]]):
    new_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
print_matrix(my_matrix)
print_matrix(matrix_transposition(my_matrix))


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def keywords_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(keywords_to_dict(first='hello world', second=12345, third=[1, 2, 3, 4, 5], fourth={'k1': 'v1', 'k2': 'v2'},
                       fifth=('1', 2, 3, 4, 5)))

# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0
operations = []


def exit_():
    print(f'Возьмите карту, на которой {account} у.е.\n'
          f'Все операции со счётом: {operations}')


def richness_check():
    global account
    percent = account * RICHNESS_TAX
    account -= percent
    operations.append(-percent)
    print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е.\n'
          f'Итого на карте {account} у.е.')


def declare_amount():
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    return amount


def deposit(amount):
    global account
    global count
    account += amount
    count += 1
    operations.append(+amount)
    print(f'Пополнение карты на {amount} у.е.\nИтого на карте {account} у.е.')


def withdraw(amount):
    global account
    global count
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                    MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    if account >= amount + withdraw_tax:
        count += 1
        account -= (amount + withdraw_tax)
        operations.append(-amount)
        print(f'Снятие с карты {amount} у.е.\nКомиссия за снятие {withdraw_tax} у.е.\n'
              f'На карте осталось {account} у.е.')
    else:
        print(f'Недостаточно денег для выполнения операции\n'
              f'Затребованная сумма {amount} у.е., Комиссия составила {withdraw_tax} у.е.\n')


def bonus():
    global account
    bonus_percent = account * ADD_PERCENT
    account += bonus_percent
    operations.append(+bonus_percent)
    print(f'На счёт начислено {ADD_PERCENT}%, составляющие {bonus_percent} у.е.\n'
          f'Итого на карте {account} у.е.')


while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        exit_()
        break
    if account > RICHNESS_SUM:
        richness_check()
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = declare_amount()
    if command == CMD_DEPOSIT:
        deposit(amount)
    elif command == CMD_WITHDRAW:
        withdraw(amount)
    if count and count % COUNT_OPER == 0:
        bonus()
