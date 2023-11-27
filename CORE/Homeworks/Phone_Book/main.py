from pathlib import Path
import json

PATH = Path.cwd() / 'contacts.json'


class PhoneBook:

    def __init__(self, record):
        self.record = Record

    try:
        with open(PATH, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except FileNotFoundError:
        with open(PATH, 'x') as file:
            file.write('{}')
        with open(PATH, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except FileExistsError:
        with open(PATH, 'r') as file:
            content = file.read()
            content_json = json.loads(content)

    except Exception:
        with open(PATH, 'w') as file:
            file.write('{}')
        with open(PATH, 'r') as file:
            content = file.read()
            content_json = json.loads(content)


class Record:
    def __init__(self):
        pass
