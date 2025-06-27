import json
from typing import TypeVar, List, Tuple


class Contact:
    """Класс Контакт"""

    def __init__(self, first_name: str, name: str, phone: str, comment: str):
        """ 
        Инициализация класса Контакт.

        Params:
            path (str): Путь к файлу справочника

        Returns:
            Contact: Объект класса
        """
        self.first_name = first_name
        self.name = name
        self.phone = phone
        self.comment = comment

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.first_name == other.first_name or self.phone == other.phone

    def __str__(self):
        return f'Фамилия: {self.first_name} | Имя:{self.name} | Телефон:{self.phone}  | Kомментарий:{self.comment}'

    def __repr__(self):
        return f'Contact(first_name = ({self.first_name}), name =({self.name}), phone = ({self.phone}), comment = ({self.comment}))'

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield (attr, value)

    @classmethod
    def from_list(cls, data: list[str]):
        return cls(*data)

    @staticmethod
    def is_valid_phone(phone):
        if not phone.startswith("+7") or len(phone) != 12:
            return False
        return True


class PhoneBook:
    """Класс для управления телефонным справочником"""
    flag_change: bool = False

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
        self.DICT_KEYS = [
            "first_name",
            "name",
            "phone",
            "comment"
        ]

    def __len__(self):
        return len(self.dict_data)

    def __getitem__(self, index):
        return self.dict_data(index)

    def __str__(self):
        pass

    def __iter__(self):
        for attr, value in self.__dict__items():
            yield (attr, dict(value))

    def next_id(self):
        return int(max(self.dict_data)) + 1 if self.dict_data else 1

    def func_create_contact(self, list_input_user: List[str], new_idx: str | None = None):
        """
        Метод класса Добавить контакт.

        Params:
            list_input_user (List[str]): Список значений полей контакта

        Returns:
            None
        """
        # new_contact = {}
        # for idx in range(len(self.DICT_KEYS)):
        #     new_contact[self.DICT_KEYS[idx]] = list_input_user[idx]

        idx = new_idx if new_idx else self.next_id()
        # self.dict_data[ind+1] = new_contact
        self.dict_data[str(idx)] = Contact.from_list(list_input_user)

    def func_find_contact(self, input_val: str) -> dict:
        """
        Метод класса Найти контакт

        Params:
            input_val (str): Строка поиска

        Returns:
            dict: Словарь найденных контактов

        """
        result = {}
        for key, contact in self.dict_data.items():

            if input_val.lower() in ' '.join(dict(contact).values()).lower():
                result[key] = contact
        return result

    def func_change_contact(self, contact_id: str, contact_data: list[str]) -> str:
        """
        Метод класса Изменить контакт

        Params:
            list_input_user (List[str]): Список значений полей контакта

        Returns:
            srt: Имя контакта

        """
        change_contact = dict(self.dict_data[contact_id]).copy()

        for idx, key in enumerate(self.DICT_KEYS):
            if contact_data[idx]:
                change_contact[key] = contact_data[idx]
            self.dict_data[contact_id] = Contact.from_list(
                list(change_contact.values()))

        return change_contact[self.DICT_KEYS[0]]

    def func_del_contact(self, contact_id: List[str]) -> tuple:
        """
        Метод класса Удалить контакт

        Params:
            contact_id (List[str]): ИД контакта

        Returns:
            tuple[bool, str]: True, Имя удаленного контакта/ False, описание ошибки

        """
        try:
            del_contact = self.dict_data.pop(contact_id[0])
            return True, dict(del_contact)[self.DICT_KEYS[0]]
        except Exception as e:
            return False, e

    def func_reading_from_file(self) -> Tuple[bool, str]:
        """
        Метод класса Зачитать из файла

        Params:
            None

        Returns:
            tuple[bool, str]: True, Пустая строка/ False, описание ошибки


        """
        try:
            with open(self.dict_path, 'r', encoding='utf-8') as file:
                result = json.load(file)

            for idx, contact in result.items():
                self.func_create_contact(contact.values(), idx)
            return True, ""
        except Exception as e:
            return False, str(e)

    def func_write_to_file(self) -> Tuple[bool, str]:
        """
        Метод класса Сохранить в файл
        Params:
            None

        Returns:
            tuple[bool, str]: True, Пустая строка/ False, описание ошибки

        """
        result = {}
        for idx, contact in self.dict_data.items():
            result[idx] = dict(contact)
        try:
            with open(self.dict_path, 'w', encoding='utf-8') as file:
                json.dump(result, file,
                          indent=4, ensure_ascii=False)
            return True, ""
        except Exception as e:
            return False, str(e)
