import json

from datetime import date


def write_json(data_dict, file_name):
    with open(file_name, 'w') as fn:
        json.dump(data_dict, fn, indent=4)
        return True
    return False


def read_json(file_name):
    with open(file_name) as fn:
        return json.load(fn)
    return False


def back_up_file():
    return True
