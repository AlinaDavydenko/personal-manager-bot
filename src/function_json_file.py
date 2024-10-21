import json
from config import PATH_TO_FILE

# функция ищет словарь по ключу, времени. Если словаря нет, создаёт новый и вписывает его в структуру json


def read_json() -> dict:
    """ функция считывает json объект """
    with open(PATH_TO_FILE) as f:
        data = json.load(f)
        return data


# функция для создания словаря в make_dict


def write_json(json_object):
    """ функция записывает в json словарь """
    with open(PATH_TO_FILE, 'w', encoding='UTF-8') as f:
        json.dump(json_object, f)


#ToDo:
# открыть файл json
# записать дату и дела
# искать данные по ключу и выдавть их
