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


# class Character:
#     hp = 100
#     mp = 100
#
#     def __init__(self, name):
#         self.name = name
#         self.right_hand = None
#         self.left_hand = None
#
#     def pick_weapon(self, weapon):
#         if self.right_hand is None:
#             self.right_hand = weapon
#         elif self.left_hand is None:
#             self.left_hand = weapon
#         else:
#             print("I can't pick any more weapons.")
#
#     def show_weapon(self):
#         print(self.right_hand, self.left_hand)
#
#     def move(self):
#         print("I'm moving.")
#
#     def attack(self):
#         if self.right_hand is None and self.left_hand is None:
#             print('I have no weapon.')
#         else:
#             print("I'm attacking.")
#
#     def defend(self):
#         if self.right_hand is None and self.left_hand is None:
#             print("I have no shield.")
#         else:
#             print("I'm defending.")
#
#
# class Weapon:
#     def __init__(self, type):
#         self.type = type
#         self.damage = 15
#
#
# char = Character('Bro')
# sword = Weapon('sword')
# shield = Weapon('shield')
#
# char.pick_weapon(sword)
# char.show_weapon()
# char.attack()
#
# char.pick_weapon(shield)
# char.show_weapon()
# char.defend()


# class Weapon:
#     def __init__(self):
#         self.damage = None
#
#     def hit(self):
#         return self.damage
#
#     def throw_weapon(self):
#         return self
#
#
# class Sword(Weapon):
#     def __init__(self):
#         super().__init__()
#         self.damage = 15
#
#
# class Axe(Weapon):
#     def __init__(self):
#         super().__init__()
#         self.damage = 20
#
#
# sword = Sword()
# axe = Axe()
#
# print(sword.hit())
# print(axe.hit())
# print(sword.throw_weapon())
# print(axe.throw_weapon())

# class Book:
#     def __init__(self, name: str, number_pages: int):
#         self.name = name
#         self.number_pages = number_pages
#         self.current_page = 0
#         self.bookmark = None
#         self.book_is_open = False
#
#     def open_book(self):
#         self.book_is_open = True
#
#     def close_book(self):
#         self.book_is_open = False
#
#     def turn_next_page(self):
#         if self.book_is_open:
#             self.current_page += 1
#
#     def turn_previous_page(self):
#         if self.book_is_open:
#             self.current_page -= 1
#
#     def bookmark_page(self):
#         self.bookmark = self.current_page
#
#     def report(self):
#         print(f"{self.name.title()}".center(25, "_"))
#         print(f"Number of pages: {self.number_pages}")
#         print(f"Current page: {self.current_page}")
#         if self.bookmark is not None:
#             print(f"Bookmarked on page: {self.bookmark}")
#
#
# book = Book("The Witcher", 1412)
#
# book.open_book()
# print(book.book_is_open)
# print(book.current_page)
# book.turn_next_page()
# print(book.current_page)
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# print(book.current_page)
# book.close_book()
# print(book.book_is_open)
# book.open_book()
# print(book.current_page)
# book.bookmark_page()
# book.report()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.turn_next_page()
# book.report()
# book.bookmark_page()
# book.report()
