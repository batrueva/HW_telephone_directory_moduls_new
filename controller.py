import view
import model
import text


def start():
    while True:
        view.show_menu()
        selection = view.func_choice_menu()
        match selection:
            case 1:
                if not model.dict_data:
                    model.func_reading_from_file()
                    view.print_message(text.file_open_text)
                    model.flag_change = False

                else:

                    if view.func_choice_open():
                        model.func_write_to_file()
                        view.print_message(text.file_save_text)
                        view.print_message(text.file_open_text)
                        model.flag_change = False
            case 2:
                model.func_write_to_file()
                view.print_message(text.file_save_text)
                model.flag_change = False
            case 3:

                view.print_contacts(model.dict_data, text.dict_empty_error)
            case 4:
                contact = view.input_user_data(text.input_menu)
                model.func_create_contact(contact)
                view.print_message(text.contact_add_message.format(contact[0]))
                model.flag_change = True
            case 5:
                contact_find = view.input_data_search(text.input_value_search)
                result = model.func_find_contact(contact_find)
                view.print_contacts(
                    result, text.error_search_message.format(contact_find))
            case 6:
                list_id_contact = view.input_user_data(
                    [text.input_id_change_contact,])
                сontact = view.input_user_data(text.input_menu)
                contact_name = model.func_change_contact(
                    list_id_contact[0], сontact)
                view.print_message(
                    text.contact_upd_message.format(contact_name))
                model.flag_change = True
            case 7:
                list_id_contact = view.input_user_data(
                    [text.input_id_del_contact,])
                contact_name = model.func_del_contact(list_id_contact)
                view.print_message(
                    text.contact_del_message.format(contact_name))
                model.flag_change = True
            case 8:
                if model.flag_change:
                    selection = view.input_user_data(
                        [text.message_out,])
                    if selection.lower() == 'n':
                        model.func_write_to_file()
                        view.print_message(text.file_save_text)
                exit()
