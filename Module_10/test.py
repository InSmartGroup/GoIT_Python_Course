# class Animal:
#     def __init__(self, animal_type: str, nickname: str, age: int, owner: str):
#         self.animal_type = animal_type
#         self.nickname = nickname.title()
#         self.age = age
#         self.owner = owner.title()
#
#     def get_info(self):
#         return f"{self.nickname} is a {self.animal_type}, it's {self.age} years old." \
#                f" {self.owner} is the {self.nickname}'s owner."
#
#     def change_age(self, new_age):
#         self.age = new_age
#         return self.age
#
#
# cat = Animal('cat', 'flash', 1, 'steve')
# dog = Animal('dog', 'light', 3, 'bob marley')
#
# print(cat.get_info())
# print(dog.get_info())
# cat.change_age(5)
# print(cat.get_info())

class Character:
    def __init__(self):
        pass