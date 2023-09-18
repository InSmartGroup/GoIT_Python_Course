from collections import UserDict


class Field:
    pass


class Phone(Field):
    pass


class Name(Field):
    pass


class Record:
    def add_phone(self):
        pass

    def remove_phone(self):
        pass

    def edit_phone(self):
        pass

    def find_phone(self):
        pass


class AddressBook(UserDict):
    def add_record(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass
