def lookup_key(data: dict, value):
    keys = []

    for k, v in data.items():
        if v == value:
            keys.append(k)

        else:
            continue

    return keys
