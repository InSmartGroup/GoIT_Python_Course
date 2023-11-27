import random

goods = ["great", "wonderful", "amazing", "good"]
bads = ["bad", "unpleasant", "shitty", "ugly", "fucked up"]
closers = ["enjoy", "have fun", "all the best", "best regards", "warmest"]

email = "I have some good results for you. Not bad. Enjoy."


def check(l, text):
    for i in l:
        if i in text.lower():
            text = text.replace(i, random.choice(l))

    return text


new_email = check(goods, email)
new_email = check(bads, new_email)
new_email = check(closers, new_email)
print(new_email)
