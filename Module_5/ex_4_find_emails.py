import re

emails_list = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org"\
               "first.middle.last@iana.or a@test.com abc111@test.com.net"


def find_all_emails(text):
    pattern = r"[A-Za-z][A-Za-z0-9._]{1,}@[A-Za-z0-9-]+\.[A-Za-z]{2,}"

    result = re.findall(pattern, text)

    return result


print(find_all_emails(emails_list))
