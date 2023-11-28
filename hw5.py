# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def pathfinder(file_path: str) -> tuple:
    *path, filename = file_path.split('/')
    name, extension = filename.split('.')
    return '/'.join(path) + '/', name, extension


file = 'D:/Gb/py_an/homework/hw5.py'
print(pathfinder(file))

# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
import decimal

names = ['Alex', 'Ben', 'Chris']
bets = [20000, 10000, 30000]
rewards = ['5.5%', '10.25%', '3.14%']

my_dict = {name: bet * decimal.Decimal(reward[:-1]) / 100 for name, bet, reward in zip(names, bets, rewards)}
print(my_dict)


# 4. Создайте функцию генератор чисел Фибоначчи


def fib(nn: int):
    first, second = 0, 1
    for _ in range(nn):
        yield first
        first, second = second, first + second


for number in fib(int(input('Введите нужное количество чисел Фибоначчи: '))):
    print(number, end=' ')
