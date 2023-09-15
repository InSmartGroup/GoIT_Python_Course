from collections import UserDict


# creating classes
class AddressBook(UserDict):
    def add_record(self, Record):
        self.data[Record.name.value] = Record


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, remove_phone):
        for phone in self.phones:
            if phone.value == remove_phone:
                self.phones.remove(phone)

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone == old_phone:
                self.phones.remove(phone)
                self.phones.append(new_phone)


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    ...


class Phone(Field):
    ...


# create new class instances
address_book = AddressBook()

phone_book = {}


# a decorator to process possible errors
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Contact not found. Please check your input.\n'
        except ValueError:
            return "Invalid input. Please enter a name followed by a phone number.\n"
        except IndexError:
            return "Invalid input. Please enter a name followed by a phone number.\n"

    return wrapper


# add a new contact
@input_error
def add_contact(name, number):
    if name in phone_book:
        raise ValueError

    else:
        phone_book[name] = number

        return f'{name.title()} with a phone number {number} has been added.\n'


# change existing phone number
@input_error
def change_phone_number(name, number):
    if name not in phone_book:
        raise KeyError

    else:
        phone_book[name] = number

        return f"{name}'s phone number has been changed to {number}.\n"


# get contact's phone number
@input_error
def get_phone_number(name):
    if name not in phone_book:
        raise KeyError

    else:
        return f"{name}'s phone number is {phone_book[name]}.\n"


# display the phone book
@input_error
def show_phone_book():
    if not phone_book:
        raise ValueError

    else:
        contact = 'Your phone book'.center(40,"-") + '\n'
        for name, number in phone_book.items():
            contact += f"{name.title()}".ljust(20) + f"{number}".rjust(20) + "\n"

    return contact


# get the list of available commands
@input_error
def get_help():
    print("Type one of the following commands".center(100, '-'))
    print(f"add <name> <phone number>".ljust(30), "to add a new contact".rjust(70))
    print(f"phone <name>".ljust(30), "to display a specified phone number".rjust(70))
    print(f"change <name> <phone number>".ljust(30), "to change a phone number of a specified contact".rjust(70))
    print(f"show all".ljust(30), "to see all the contact details".rjust(70))
    print(f"delete all".ljust(30), "to permanently delete all the contact details from the list".rjust(70))
    print(f"".ljust(100, "_"))


# the main loop
def main():
    print("Greetings! I'm CLI - your virtual assistant!")
    print("Please enter your command. Or type 'help' to get the list of commands.\n")

    commands = {
        "hello": lambda: print("How can I help you?\n"),

        "add": lambda: print(add_contact(split_user_input[1], split_user_input[2])) if
        len(split_user_input) == 3 else print("Please enter a name followed by a phone number.]n"),

        "change": lambda: print(change_phone_number(split_user_input[1], split_user_input[2])) if
        len(split_user_input) == 3 else print("Error: enter name and number.\n"),

        "phone": lambda: print(get_phone_number(split_user_input[1])) if len(split_user_input) == 2
        else print("Contact not found.\n"),

        "show all": lambda: print(show_phone_book()) if phone_book
        else print("Your phone book is empty. Please add new contacts first.\n"),

        "good bye": lambda: print("Good bye!"),

        "close": lambda: print("Good bye!"),

        "exit": lambda: print("Good bye!"),

        "quit": lambda: print("Good bye!"),

        'help': lambda: get_help()
    }

    while True:
        user_input = input('Enter command: ')
        split_user_input = user_input.split(maxsplit=2)
        user_command = split_user_input[0].strip().lower()

        if user_command in commands:
            commands[user_command]()

            if user_command in ['close', 'exit', 'quit']:
                break

        elif user_input.lower() in commands:
            commands[user_input.lower()]()

            if user_input.lower() == 'good bye':
                break

        else:
            print("Invalid command. Please type 'help' to see the list of commands.\n")


if __name__ == '__main__':
    main()
