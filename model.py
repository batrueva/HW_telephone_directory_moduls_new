import json
import text
from typing import TypeVar, List, Tuple
"""
Суммирует два числа.

Args:
    a (int): Первое число
    b (int): Второе число

Returns:
    int: Сумма двух чисел
"""


class PhoneBook:
    """Класс для управления телефонным справочником"""
    flag_change: bool = False
    DICT_KEYS = [
        "first_name",
        "name",
        "phone",
        "comment"
    ]

    def __init__(self, path: str):
        """
        Инициализация класса Тел. справочник.

        Params:
            path (str): Путь к файлу справочника

        Returns:
            PhoneBook: Объект класса
        """
        self.dict_path: str = path
        # 'Telefon_directory.json'ss
        self.dict_data: dict = {}

    def func_create_contact(self, list_input_user: List[str]):
        """
        Метод класса Добавить контакт.

        Params:
            list_input_user (List[str]): Список значений полей контакта

        Returns:
            None
        """
        new_contact = {}
        for idx in range(len(self.DICT_KEYS)):
            new_contact[self.DICT_KEYS[idx]] = list_input_user[idx]

        ind = int(max(self.dict_data)) if self.dict_data else 0
        self.dict_data[ind+1] = new_contact

    def func_find_contact(self, input_val: str):
        """
        Метод класса Найти контакт

        Params:
            list_input_user (List[str]): Список значений полей контакта

        Returns:


        """
        result = {}
        for key, contact in self.dict_data.items():

            if input_val.lower() in ' '.join(contact.values()).lower():
                result[key] = contact

        return result

    def func_change_contact(self, contact_id: str, contact_data: list[str]) -> str:
        """Метод класса Контакт.Изменить контакт"""
        change_contact = self.dict_data[contact_id].copy()

        for idx, key in enumerate(self.DICT_KEYS):
            if contact_data[idx]:
                change_contact[key] = contact_data[idx]
            self.dict_data[contact_id] = change_contact

        return change_contact["name"]

    def func_del_contact(self, contact_id: List[str]) -> tuple:
        """Метод класса Контакт.Удалить контакт"""
        try:
            del_contact = self.dict_data.pop(contact_id[0])
            return True, del_contact[self.DICT_KEYS[1]]
        except Exception as e:
            return False, e

    def func_reading_from_file(self) -> Tuple:
        """Метод класса Контакт.Зачитать из файла"""
        try:
            with open(self.dict_path, 'r', encoding='utf-8') as file:
                self.dict_data = json.load(file)

            return True, ""
        except Exception as e:
            return False, e

    def func_write_to_file(self) -> Tuple:
        """Метод класса Контакт.Сохранить в файл"""
        try:
            with open(self.dict_path, 'w', encoding='utf-8') as file:
                json.dump(self.dict_data, file, indent=4, ensure_ascii=False)
            return True, ""
        except Exception as e:
            return False, e
