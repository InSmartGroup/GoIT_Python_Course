import json
from pathlib import Path

PATH = Path.cwd() / "contacts.json"


def check_file_status_and_read(path):
    """
    Checks if the file exists and reads it's content.
    If the file doesn't exist, it will be automatically created. Thus, the dictionary will be empty.

    :param path: A path to a .json file that stores your contact details.
    :type path: A pathlib.Path object

    :return: A dictionary with all the contact details.
    :rtype: dict
    """
    try:
        with open(path, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except FileNotFoundError:
        with open(path, 'x') as file:
            file.write('{}')
        with open(path, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except FileExistsError:
        with open(path, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except Exception:
        with open(path, 'w') as file:
            file.write('{}')
        with open(path, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    return content_json


def write_to_file(path, data_to_write):
    """
    Writes user's input to a file.

    :param path: A path to a .json file that stores your contact details.

    :param data_to_write: User's input.
    :type data_to_write: dict
    """
    with open(path, 'w') as file:
        file.write(json.dumps(data_to_write))


def get_input_from_user():
    """
    Returns an input from a user.

    :return: User input.
    :rtype: str
    """
    i = input("Enter command: ").lower()
    return i


def user_input_to_list(user_input: str):
    """
    Splits the user's input and returns a list.

    :param user_input: User input.
    :type user_input: str

    :return: User's input in a form of a list.
    :rtype: list
    """
    user_input_list = user_input.strip().split()
    return user_input_list


def add_contact(user_input: list, file_data: dict):
    """
    Adds new contact details to a list of contacts.
    It should be done by typing the word 'add' followed by a name and a phone number.
    E.g.: add William +18007717782

    :param user_input: User's input in a form of a list.
    :type user_input: list

    :param file_data: A dictionary that contains your contact details.
    :type file_data: dict

    :return: An updated dictionary with a new contact added.
    :rtype: dict
    """
    if user_input[1] not in file_data:
        file_data[user_input[1]] = user_input[2]
    else:
        print(f"There is a contact named {user_input[1].title()} already.\n")

    return file_data


def show_contact_phone(user_input: list, file_data: dict):
    """
    Displays a phone number of a specific contact.
    It should be done by typing the word 'phone' followed by a name of a contact.
    E.g.: phone William

    :param user_input: User's input in a form of a list.
    :type user_input: list

    :param file_data: A dictionary that contains your contact details.
    :type file_data: dict
    """
    if user_input[1] in file_data:
        print(f"{user_input[1].title()}'s phone number is {file_data[user_input[1]]}.")
    else:
        print(f"There is no contact named {user_input[1].title()}. Add a contact first.\n")


def show_all_contacts(file_data: dict):
    """
    Displays all the contacts from your contact list, one by one.
    It should be done by typing 'show all'.
    E.g.: show all

    :param file_data: A dictionary that contains your contact details.
    :type file_data: dict
    """
    if len(file_data) > 0:
        if len(file_data) == 1:
            print(f"There is {len(file_data)} contact in your list".center(50, "_"))
        else:
            print(f"There are {len(file_data)} contacts in your list".center(50, "_"))

        for key, value in file_data.items():
            print(f"{key.title()}".ljust(15), f"{value}".rjust(35))
        print()

    else:
        print("Your list is empty. Add new contacts first.\n")


def change_contact_phone(user_input: list, file_data: dict):
    """
    Changes a single phone number in a list of contacts.
    It should be done by typing the word 'change' followed by a name and a new phone number.
    E.g.: change William +18007717782

    :param user_input: User's input in a form of a list.
    :type user_input: list

    :param file_data: A dictionary that contains your contact details.
    :type file_data: dict

    :return: An updated dictionary with a new phone number.
    :rtype: dict
    """
    if user_input[1] in file_data:
        file_data[user_input[1]] = user_input[2]
    else:
        print(f"There is no contact named {user_input[1]}.")

    return file_data


def delete_all_contacts(file_data):
    """
    Permanently deletes all the records in the contact list.
    It should be done by typing the 'delete all' and then typing 'Y' to confirm your choice.

    :param file_data: A dictionary that contains your contact details.
    :type file_data: dict

    :return: If confirmed - a new dictionary with no items in it. If not - returns an old dictionary.
    :rtype: dict
    """
    input_confirmation = input("Are you sure you want to delete all the contact details? Type [Y / N]: ")

    if input_confirmation == 'Y':
        file_data = {}
        print("All contacts have been deleted.\n")
        return file_data

    else:
        return file_data


def get_help():
    """
    Displays key commands to control the CLI assistant.
    It should be done by typing the word "help".
    """
    print("Type one of the following commands".center(100, '-'))
    print(f"add <name> <phone number>".ljust(30), "to add a new contact".rjust(70))
    print(f"phone <name>".ljust(30), "to display a specified phone number".rjust(70))
    print(f"change <name> <phone number>".ljust(30), "to change a phone number of a specified contact".rjust(70))
    print(f"show all".ljust(30), "to see all the contact details".rjust(70))
    print(f"delete all".ljust(30), "to permanently delete all the contact details from the list".rjust(70))
    print(f"".ljust(100, "_"))


def main():
    while True:
        file_content = check_file_status_and_read(PATH)

        user_input = get_input_from_user()
        if user_input == 'quit' or user_input == 'exit' or user_input == 'close' or user_input == 'bye':
            break

        user_input_list = user_input_to_list(user_input)
        if user_input_list[0] == 'add':
            file_content = add_contact(user_input_list, file_content)
        elif user_input_list[0] == 'phone':
            show_contact_phone(user_input_list, file_content)
        elif user_input_list[0] == 'show' and user_input_list[1] == 'all':
            show_all_contacts(file_content)
        elif user_input_list[0] == 'change':
            file_content = change_contact_phone(user_input_list, file_content)
        elif user_input == 'help':
            get_help()
        elif user_input == 'delete all':
            file_content = delete_all_contacts(file_content)

        write_to_file(PATH, file_content)


if __name__ == "__main__":
    print("Greetings! I'm CLI - your virtual assistant!")
    print("Please enter your command. Or type 'help' to get the list of commands.")

    main()
