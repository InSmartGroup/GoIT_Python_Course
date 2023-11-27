def get_input_from_user():
    i = input("Enter command: ").lower()
    return i


def user_input_to_list(user_input: str):
    user_input_list = user_input.strip().split()
    return user_input_list


def add_contact(user_input: list, file_data: dict):
    if user_input[1] not in file_data:
        if user_input[2].isdigit():
            file_data[user_input[1]] = user_input[2]
            print(f"{user_input[1].title()} has been added to your contact list.\n")
        else:
            print(f"{user_input[2]} is not a number.")
            print("Type 'add' followed by a name and a phone number of a person you want to add.\n")

    else:
        print(f"There is a contact named {user_input[1].title()} already.\n")

    return file_data


def show_contact_phone(user_input: list, file_data: dict):
    if user_input[1] in file_data:
        print(f"{user_input[1].title()}'s phone number is {file_data[user_input[1]]}.\n")
    else:
        print(f"There is no contact named {user_input[1].title()}. Add a contact first.\n")


def show_all_contacts(file_data: dict):
    if len(file_data) > 0:
        if len(file_data) == 1:
            print(f"There is {len(file_data)} contact in your list".center(50, "_"))
        else:
            print(f"There are {len(file_data)} contacts in your list".center(50, "_"))

        for key, value in file_data.items():
            print(f"{key.title()}".ljust(15), f"{value}".rjust(35))
        print()

    else:
        print("Your list of contacts is empty. Add new contacts first.")
        print("Type 'add' followed by a name and a phone number of a person you want to add.\n")


def change_contact_phone(user_input: list, file_data: dict):
    if user_input[1] in file_data:
        file_data[user_input[1]] = user_input[2]
        print(f"{user_input[1].title()}'s phone number has been changed to {user_input[2]}.\n")
    else:
        print(f"There is no contact named {user_input[1]}.\n")

    return file_data


def delete_all_contacts(file_data):
    input_confirmation = input("Are you sure you want to delete all the contact details? Type [Y / N]: ")

    if input_confirmation == 'Y':
        file_data = {}
        print("All contacts have been deleted.\n")
        return file_data

    else:
        return file_data


def get_help():
    print("Type one of the following commands".center(100, '-'))
    print(f"add <name> <phone number>".ljust(30), "to add a new contact".rjust(70))
    print(f"phone <name>".ljust(30), "to display a specified phone number".rjust(70))
    print(f"change <name> <phone number>".ljust(30), "to change a phone number of a specified contact".rjust(70))
    print(f"show all".ljust(30), "to see all the contact details".rjust(70))
    print(f"delete all".ljust(30), "to permanently delete all the contact details from the list".rjust(70))
    print(f"".ljust(100, "_"))


def error_processing(error):
    if error:
        print("Please revise your input. Use the 'help' command to get the full list of commands.\n")


def main():
    print("Greetings! I'm CLI - your virtual assistant!")
    print("Please enter your command. Or type 'help' to get the list of commands.\n")

    contacts_dict = {}

    while True:
        try:
            user_input = get_input_from_user()
            if user_input == 'quit' or user_input == 'exit' or user_input == 'close' or user_input == 'bye':
                print("Thank you for using CLI. Have a blessed day!")
                break

            user_input_list = user_input_to_list(user_input)
            if user_input_list[0] == 'add':
                contacts_dict = add_contact(user_input_list, contacts_dict)

            elif user_input_list[0] == 'phone':
                show_contact_phone(user_input_list, contacts_dict)

            elif user_input == 'show all':
                show_all_contacts(contacts_dict)

            elif user_input_list[0] == 'change':
                contacts_dict = change_contact_phone(user_input_list, contacts_dict)

            elif user_input == 'help':
                get_help()

            elif user_input == 'delete all':
                contacts_dict = delete_all_contacts(contacts_dict)

            elif user_input == 'hello':
                print("Hello to you too! How can I help you?\n")

            elif user_input[0] != 'add' or user_input[0] != 'phone' or user_input[0] != 'change':
                print("Unrecognized command. Please use help by typing 'help' in the command prompt.\n")

        except IndexError or ValueError or TypeError as error:
            error_processing(error)


if __name__ == "__main__":
    main()
