contacts_dict = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found.\n"
        except ValueError:
            return "Invalid input. Please enter a name followed by a phone number.\n"
        except IndexError:
            return "Invalid input. Please enter a name followed by a phone number.\n"

    return inner


@input_error
def add_contact(name, phone):
    if name in contacts_dict:
        raise ValueError
    contacts_dict[name] = phone
    return f"{name.title()} has been added to the contact list.\n"


@input_error
def change_phone(name, phone):
    if name not in contacts_dict:
        raise KeyError
    else:
        contacts_dict[name] = phone
        return f"{name.title()}'s phone number has been changed to {phone}.\n"


@input_error
def get_phone(name):
    if name not in contacts_dict:
        raise KeyError
    return (f"{name.title()}'s phone number is {contacts_dict[name]}.\n")


@input_error
def show_all_contacts():
    if not contacts_dict:
        raise ValueError
    result = "Contacts:\n"
    for name, phone in contacts_dict.items():
        result += f"{name}: {phone}\n"
    return result


def get_help():
    print("Type one of the following commands".center(100, '-'))
    print(f"add <name> <phone number>".ljust(30), "to add a new contact".rjust(70))
    print(f"phone <name>".ljust(30), "to display a specified phone number".rjust(70))
    print(f"change <name> <phone number>".ljust(30), "to change a phone number of a specified contact".rjust(70))
    print(f"show all".ljust(30), "to see all the contact details".rjust(70))
    print(f"delete all".ljust(30), "to permanently delete all the contact details from the list".rjust(70))
    print(f"".ljust(100, "_"))


def print_error(message):
    print(f"Error: {message}")


def main():
    commands_dict = {
        "hello": lambda: print("How can I help you?\n"),
        "good bye": lambda: print("Thank you for using CLI!"),
        "close": lambda: print("Thank you for using CLI!"),
        "exit": lambda: print("Thank you for using CLI!"),
        "show all": lambda: print(show_all_contacts()),
        "add": lambda: print(add_contact(user_input_split[1], user_input_split[2])) if len(user_input_split) == 3 \
        else print_error("Please type a name followed by a phone number.\n"),
        "change": lambda: print(change_phone(user_input_split[1], user_input_split[2])) if len(
            user_input_split) == 3 else print_error("write name and phone."),
        "phone": lambda: print(get_phone(user_input_split[1])) if len(user_input_split) == 2 else print_error(
            "write name."),
        'help': lambda: print(get_help()),
    }

    while True:
        user_input = input("Enter command: ")
        user_input_split = user_input.split(maxsplit=2)
        output_text = ""
        for char in user_input:
            if char != " ":
                output_text += char.lower()
            else:
                break

        if output_text in commands_dict:
            commands_dict[output_text]()
            if output_text in ["close", "exit"]:
                break

        elif user_input.lower() in commands_dict:
            commands_dict[user_input.lower()]()
            if user_input.lower() == "good bye":
                break

        else:
            print("Unrecognized command. Please type 'help' to get the full list of commands.\n")


if __name__ == '__main__':
    main()
