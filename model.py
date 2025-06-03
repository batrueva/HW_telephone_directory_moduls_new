import json
import text

dict_path: str = 'Telefon_directory.json'
dict_data: dict = {}
flag_change: bool = False
DICT_KEYS = [
    "first_name",
    "name",
    "phone",
    "comment"
]


def func_create_contact(list_input_user: list[str]):

    new_contact = {}
    for idx in range(len(DICT_KEYS)):
        new_contact[DICT_KEYS[idx]] = list_input_user[idx]

    ind = max(dict_data)+1
    dict_data[ind] = new_contact


def func_find_contact(input_val: str):
    result = {}
    for key, value in dict_data.items():
        if input_val.lower() in value.values().lower():
            result[key] = value
    return result


def func_change_contact(contact_id: int, contact_data: list[str]):

    change_contact = dict_data[int(contact_id)].copy()
    for idx, key in enumerate(DICT_KEYS):
        if contact_data[idx]:
            change_contact[key] = contact_data[idx]
        dict_data[contact_id] = change_contact

    return change_contact["name"]


def func_del_contact(contact_id: int):

    del_contact = dict_data.pop(int(contact_id))
    return del_contact["name"]


def func_reading_from_file():

    with open(dict_path, 'r', encoding='utf-8') as file:
        dict_data = json.load(file)


def func_write_to_file():

    with open(dict_path, 'w', encoding='utf-8') as file:
        json.dump(dict_data, file, indent=4, ensure_ascii=False)
