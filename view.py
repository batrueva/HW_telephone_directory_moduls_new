import text
from customException import InvalidChoiceMenu, InvalidInputUser


def show_menu():
    """
    Метод класса Вывод меню в консоль.

    Params:
        None

    Returns:
        None
    """
    for idx, item in enumerate(text.main_menu):
        if idx:
            print(f'{idx}.{item}')
        else:
            print(item)


def func_choice_menu():
    """
    Метод класса Выбор пункта меню.

    Params:
        None

    Returns:
        None
    """
    while (True):
        try:
            selection = input(text.menu_input_mess)
            if selection and selection in [str(x) for x in range(1, len(text.main_menu))]:
                return int(selection)
            else:
                raise InvalidChoiceMenu(text.menu_input_mess)
        except InvalidInputUser as e:
            print_message(' '.join([text.error_message, str(e),]))


def print_message(msg: str):
    """
    Метод класса Вывод форматированного сообщения.

    Params:
        msg; str

    Returns:
        None
    """
    print("----------------------------------------")
    print(msg)
    print("----------------------------------------")


def func_choice_open() -> bool:
    """
    Метод класса Ввод выбора пользователя.

    Params:
        None

    Returns:
        bool
    """
    selection = input(text.file_open_not_empty)
    if selection.lower() == 'y':
        return True
    return False


def print_contacts(dict_data, message):
    """
    Метод класса Вывод справочника в консоль.

    Params:
        dict_data (Dict): Справочник контактов
        message (str): Сообщение пользователю

    Returns:
        None
    """
    if dict_data:
        print("\nСписок контактов:\n")
        print("--------------------------------------------------------------------------------")
        for key, contact in dict_data.items():
            print(f"ИД: {key} |  {contact}")
            print(
                "--------------------------------------------------------------------------------")
        print("\n\n")
    else:
        print_message(message)


def input_user_data(messages: list[str]):
    """
    Метод класса Ввод данных контакта.

    Params:
        dict_data (Dict): Справочник контактов
        message (str): Сообщение пользователю

    Returns:
        None
    """
    result = []
    for entry in messages:
        result.append(input(entry))
    return result
