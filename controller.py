import view
import model
import text
from customException import InvalidContactData, InvalidInputUser


def start():
    pb = model.PhoneBook('Telefon_directory.json')
    while True:

        view.show_menu()
        selection = view.func_choice_menu()

        def open_file():

            if pb.dict_data:
                if view.func_choice_open():
                    pb.func_write_to_file()
                    view.print_message(text.file_save_sccessfully)
            result, error = pb.func_reading_from_file()

            if result:
                view.print_message(text.file_open_successfully)
            else:
                view.print_message(text.file_open_error.format(error))
            pb.flag_change = False

        def save_file():
            pb.func_write_to_file()
            view.print_message(text.file_save_sccessfully)
            pb.flag_change = False

        def output_contacts():

            view.print_contacts(pb.dict_data, text.dict_empty_error)

        def create_contact():
            try:
                contact = view.input_user_data(text.input_menu)
                # проверка пустого контакта
                if not ' '.join(contact).lstrip():
                    raise InvalidContactData(text.contact_data_empty)
                # проверка формата номера телефона
                if not model.Contact.is_valid_phone(contact[2]):
                    raise InvalidContactData(text.contact_phone_error)
                pb.func_create_contact(contact)
                view.print_message(text.contact_add_message.format(contact[0]))
                pb.flag_change = True
            except InvalidContactData as e:
                view.print_message(str(e))

        def find_contact():
            try:
                contact_find = view.input_user_data([text.input_value_search,])
                if contact_find[0]:
                    result = pb.func_find_contact(contact_find[0])
                    view.print_contacts(
                        result, text.error_search_message.format(contact_find))
                else:
                    raise InvalidInputUser(text.error_message)
            except InvalidInputUser as e:
                view.print_message(e)

        def change_contact():
            try:
                list_id_contact = view.input_user_data(
                    [text.input_id_change_contact,])
                if list_id_contact[0] in pb.dict_data:
                    сontact = view.input_user_data(text.input_menu)
                    contact_name = pb.func_change_contact(
                        list_id_contact[0], сontact)
                    pb.flag_change = True

                    view.print_message(
                        text.contact_upd_message.format(contact_name))
                else:
                    raise InvalidInputUser(text.error_message)
            except InvalidInputUser as e:
                view.print_message(e)

        def del_contact():
            try:
                list_id_contact = view.input_user_data(
                    [text.input_id_del_contact,])
                if list_id_contact[0] in pb.dict_data.keys():
                    result, contact_name = pb.func_del_contact(list_id_contact)
                    if result:
                        pb.flag_change = True
                        view.print_message(
                            text.contact_del_message.format(contact_name))
                    else:
                        raise InvalidContactData(
                            text.contact_del_error.format(contact_name))
                else:
                    raise InvalidInputUser(text.error_message)
            except InvalidInputUser as e:
                view.print_message(e)
            except InvalidContactData as e:
                view.print_message(e)

        def close_program():
            if pb.flag_change:
                try:
                    selection = view.input_user_data(
                        [text.message_out,])
                    if selection[0].lower() in ['y', 'n']:
                        if selection[0].lower() == 'y':
                            result, message_error = pb.func_write_to_file()
                            if result:
                                view.print_message(text.file_save_sccessfully)
                                exit()
                            else:
                                raise Exception(
                                    text.file_save_error.format(message_error))
                        else:
                            exit()

                    else:
                        raise InvalidInputUser(text.error_message)
                except InvalidInputUser as e:
                    view.print_message(e)
                except Exception as e:
                    view.print_message(e)
            else:
                exit()
        menu_items_funcs = [
            open_file,
            save_file,
            output_contacts,
            create_contact,
            find_contact,
            change_contact,
            del_contact,
            close_program,
        ]
        menu_items_funcs[selection - 1]()
