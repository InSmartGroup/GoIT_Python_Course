from collections import UserDict


class AddressBook(UserDict):
    data = {}

    def add_record(self, record: str):
        name = record.split()[0].title()
        phone_number = record.split()[1]
        self.data[name] = phone_number

    def find(self, contact_name: str):
        return self.data[contact_name.title()]

    def delete(self, contact_name: str):
        del self.data[contact_name.title()]


address_book = AddressBook()
address_book.add_record('greg 0955477130')
address_book.add_record('sveta 0955477131')
print(address_book.data)
print(address_book.find('greg'))

address_book.delete('greg')
print(address_book.data)
