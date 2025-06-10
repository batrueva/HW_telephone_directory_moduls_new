import view
import model
import text


def start():
    pb = model.PhoneBook('Telefon_directory.json')
    while True:

        view.show_menu()
        selection = view.func_choice_menu()

        def open_file():

            if not pb.dict_data:
                result, error = pb.func_reading_from_file()

                if result:
                    view.print_message(text.file_open_successfully)
                else:
                    view.print_message(text.file_open_error.format(error))
                pb.flag_change = False

            else:

                if view.func_choice_open():
                    pb.func_write_to_file()
                    view.print_message(text.file_save_text)
                    view.print_message(text.file_open_successfully)
                    pb.flag_change = False

        def save_file():
            pb.func_write_to_file()
            view.print_message(text.file_save_text)
            pb.flag_change = False

        def output_contacts():

            view.print_contacts(model.dict_data, text.dict_empty_error)

        def create_contact():
            contact = view.input_user_data(text.input_menu)
            pb.func_create_contact(contact)
            view.print_message(text.contact_add_message.format(contact[0]))
            pb.flag_change = True

        def find_contact():
            contact_find = view.input_data_search(text.input_value_search)
            result = pb.func_find_contact(contact_find)
            view.print_contacts(
                result, text.error_search_message.format(contact_find))

        def change_contact():
            list_id_contact = view.input_user_data(
                [text.input_id_change_contact,])
            сontact = view.input_user_data(text.input_menu)
            contact_name = pb.func_change_contact(
                list_id_contact[0], сontact)
            view.print_message(
                text.contact_upd_message.format(contact_name))
            pb.flag_change = True

        def del_contact():
            list_id_contact = view.input_user_data(
                [text.input_id_del_contact,])
            result, contact_name = pb.func_del_contact(list_id_contact)
            if result:
                view.print_message(
                    text.contact_del_message.format(contact_name))
            else:
                view.print_message(
                    text.contact_del_error.format(contact_name))
            pb.flag_change = True

        def close_program():
            if pb.flag_change:
                selection = view.input_user_data(
                    [text.message_out,])
                if selection.lower() == 'n':
                    pb.func_write_to_file()
                    view.print_message(text.file_save_text)
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
