import os

import CRUD_json
import default_data


def get_data_from_json(file_name):
    return CRUD_json.read_json(file_name) if file_name in os.listdir() else default_data.NEW_DATA


def update_data(data, key, val):
    if isinstance(data[key], list):
        data[key].append(val)
    else:
        data[key] = val  # get_date_in_string()
    return data


def send_data_to_json(data, file_name):
    return CRUD_json.write_json(data, file_name)


if __name__ == "__main__":

    abc = get_data_from_json('xyz.json')
    print(abc)

    abc = update_data(abc, 'edited on', '2020-09-05')

    abc = update_data(abc, 'products', {'date': '2020-09-05'})

    abc = send_data_to_json(abc, 'xyz.json')
