# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

from pathlib import Path
import csv
import json
import pickle
import os


def get_dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as catalog:
        for entry in catalog:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def direct_info(direct: Path) -> None:
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with (open('result.json', 'w') as f_json,
          open('result.csv', 'w', newline='', encoding='utf-8') as f_csv,
          open('result.pickle', 'wb') as f_pickle):
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            for dir in dir_name:
                size = get_size(dir_path + '/' + dir)
                json_data[dir_path].update({dir: {'size': size, 'file_or_dir': 'directory'}})
                rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
            for fi in file_name:
                size = get_size(dir_path + '/' + fi)
                json_data[dir_path].update({fi: {'size': size, 'file_or_dir': 'file'}})
                rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


if __name__ == '__main__':
    direct_info(Path('D:\\Gb\\py_an\\hw8'))


# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=2)


def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(f'{file.stem}.pickle', 'wb') as f_writebyte:
                pickle.dump(data, f_writebyte)


def pickle_to_csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


def csv_to_pickle(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f_read:
        csv_file = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))
