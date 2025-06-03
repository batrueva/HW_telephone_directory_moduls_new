import text


def show_menu():
    for idx, item in enumerate(text.main_menu):
        if idx:
            print(f'{idx}.{item}')
        else:
            print(item)


def func_choice_menu():
    while (True):
        try:
            selection = int(input(text.menu_input_mess))
            if selection in range(1, len(text.main_menu)):
                return selection
            else:
                print(text.error_message)
        except ValueError:
            print(text.menu_input_mess)


def print_message(msg):
    print("\n-------------------------\n")
    print(msg)
    print("\n-------------------------\n")


def func_choice_open():
    selection = input(text.file_open_error)
    if selection.lower() == 'y':
        return True
    return False


def print_contacts(dict_data, message):
    if dict_data:
        for key, value in dict_data.items():
            print(f"ИД: {key}")
            for key1, value1 in value.items():
                print_message(f"\t{key1}  : {value1} ")
            print("\n-------------------------\n")
        print("\n\n")
    else:
        print_message(message)


def input_user_data(messages: list[str]):
    result = []
    for entry in messages:
        result.append(input(entry))
    return result


def add_contact_message(message: str):
    print_message(message)


def input_data_search(message):
    return input(message).strip()


if __name__ == '__main__':
    show_menu()
