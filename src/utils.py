import json
from config import PATH_TO_FILE


def find_data_in_json(dict_json: dict, key: str):
    """ функция ищет значение по ключу """
    return dict_json.get(key, 0)
