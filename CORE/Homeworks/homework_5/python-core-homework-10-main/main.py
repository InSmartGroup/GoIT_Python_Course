from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("This field can't be empty.")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("A phone number must contain 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [i for i in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

        raise ValueError(f"Phone number '{old_phone}' not found.")

    def find_phone(self, phone):
        phones_found = [i for i in self.phones if p.value == phone]

        return phones_found[0] if phones_found else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phone number: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# the main loop
if __name__ == "__main__":
    address_book = AddressBook()
