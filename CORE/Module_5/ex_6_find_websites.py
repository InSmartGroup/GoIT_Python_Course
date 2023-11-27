import re


def find_all_links(text):
    pattern = r"https://[A-Za-z0-1]+[.][A-Za-z0-9]+[.][A-Za-z]+|http://[A-Za-z0-9]+[.][A-Za-z]+"
    result = re.findall(pattern, text)

    return result
