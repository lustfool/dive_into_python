# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv


def _is_not_leap(year: int) -> bool:
    return not (year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def check_date(full_date: str) -> bool:
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 29:
        return False
    elif month == 2 and day > 28 and _is_not_leap(year):
        return False
    else:
        return True


if __name__ == '__main__':
    date = argv[1]
    print(check_date(date))

# 3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

N = 8
x, y = [0] * N, [0] * N

for i in range(N):
    enter = input(f'Введите координаты ферзя {i + 1} через пробел: ')
    x[i], y[i] = map(int, enter.split())

for i in range(N):
    for j in range(i + 1, N):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = False
        else:
            result = True
print(result)

# 4. Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint

N = 8
NUM_CASES = 4

x, y = [0] * N, [0] * N


def set_queens(n: int = N):
    for nn in range(n):
        x[nn], y[nn] = randint(1, N + 1), randint(1, N + 1)
    return x, y


def captured(n: int = N):
    set_queens(n)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True


def show_success_cases(cases=NUM_CASES):
    success_cases = []
    while cases > 0:
        if captured():
            success_cases.append([*zip(x, y)])
            cases -= 1
    return success_cases


if __name__ == '__main__':
    for nn, coord_list in enumerate(show_success_cases(), start=1):
        print(f'{nn}: {coord_list}')
