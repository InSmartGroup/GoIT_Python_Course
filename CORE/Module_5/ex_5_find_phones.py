import re


def find_all_phones(text):
    pattern = r"\+\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}|\+\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}"

    result = re.findall(pattern, text)

    return result
