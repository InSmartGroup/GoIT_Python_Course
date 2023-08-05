articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    found_words = []

    if not letter_case:
        key = key.lower()
        for i in articles_dict:
            if key in i['title'].lower() or key in i['author'].lower():
                found_words.append(i)

    else:
        for i in articles_dict:
            if key in i['title'] or key in i['author']:
                found_words.append(i)

    return found_words


print(find_articles('ocean'))
