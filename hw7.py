# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path


def rename_files(dir_path: str | Path, new_name: str = '', count: int = 3, in_extension: str = 'txt',
                 out_extension: str = 'txt', slice_name: tuple = (0, 0)) -> None:
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    files_count = 1
    for current_file in file_list:
        name, extension = current_file.split('.')
        if extension == in_extension:
            new_file = ''
            if slice_name:
                new_file += f'{name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{out_extension}'
            os.rename(os.path.join(dir_path, current_file),
                      os.path.join(dir_path, new_file))
            files_count += 1


if __name__ == '__main__':
    rename_files(Path('D:\\Gb\\py_an\\hw7'), 'new_f', 3, 'bin', 'txt', (1, 3))

# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from random import randint, choices
from string import ascii_lowercase, digits
from os import chdir
from pathlib import Path


def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                count: int = 42) -> None:
    for _ in range(count):
        print(Path.cwd())
        while True:
            file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))) + '.' + extension
            if not Path(file_name).is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_name, 'wb') as f:
            f.write(data)


def generate_file(filepath: str | Path, **kwargs) -> None:
    if isinstance(filepath, str):
        filepath = Path(filepath)
    if not filepath.is_dir():
        filepath.mkdir(parents=True)
    chdir(filepath)
    for extension, amount in kwargs.items():
        create_file(extension, count=amount)


def sort_files(path: str | Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['mp4', 'avi', 'mkv', 'mov'],
            Path('image'): ['jpeg', 'jpg', 'png', 'gif'],
            Path('music'): ['mp3', 'wav', 'flac', 'm4a'],
            Path('text'): ['txt', 'doc']
        }
    reverse_groups = {}
    for directory, extension_list in groups.items():
        if not directory.is_dir():
            directory.mkdir()
        for extension in extension_list:
            reverse_groups[f'.{extension}'] = directory
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    generate_file('new', txt=2, bin=1)
    sort_files(Path('D:\\Gb\\py_an\\hw7\\new'))
    rename_files(Path('D:\\Gb\\py_an\\hw7\\new'), 'new_f', 3, 'txt', 'bin',
                 (1, 3))
