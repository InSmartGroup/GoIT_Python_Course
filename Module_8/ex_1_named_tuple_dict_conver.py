import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cats_list = []

    for cat in cats:
        if isinstance(cat, tuple):
            i = {'nickname': cat[0], 'age': cat[1], 'owner': cat[2]}
            cats_list.append(i)
        elif isinstance(cat, dict):
            i = Cat(cat['nickname'], cat['age'], cat['owner'])
            print(i)
            cats_list.append(i)

    return cats_list


cats_to_dict = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_to_named = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

print(convert_list(cats_to_named))
