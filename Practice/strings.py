import string
import time

print(string.whitespace)
print(string.punctuation)

st1 = "  !!! What the ... ?!! Get out of here, you bastard!"
st2 = "  !!! What the ... ?!! "
print(st1.strip(string.punctuation))
print(st2.strip(string.punctuation + string.whitespace))

st3 = "Dobriy den everybody! Slava Ukraine! Geroyam slava! Slava, Slava, Slava!"
print(st3)
print(f"Slava: {st3.count('Slava')}")
st3 = st3.replace("Slava", "Glory to", 1)
print(st3)
print(st3.replace("Slava", "Glory", 3))

st4 = "Hi! My name is who? My name is what? My name is Slim Shady..."
print(st4.lower())
print(st4.upper())
print(st4.capitalize())
print(st4.title())
print(st4.swapcase())

st5 = "Dobriy den everybody"
print(st5.center(30, "_"))
print(st5.rjust(30, "_"))
print(st5.ljust(30, "_"))
print(f"{"".ljust(10, "*")}{"".center(10, "_")}{"".rjust(10, "*")}")

# formatting, old, shitty
name = "Gregory"
age = 37
print("Hello! My name is %s." % name)
print("Hello! My name is %s. I'm %d years old." % (name, age))

# formatting, newer, much better
print("Hello! My name is {}.".format(name))
print("Hello! My name is {name}. I'm {age} years old.".format(name=name, age=age))

# formatting, f-strings, the newest, the best
print(f"Hello! My name is {name}.")
print(f"Hello! My name is {name}. I'm {age} years old.")
print(f"My name is {name:.>15}. I'm {age:.^15} years old.")
print(f"{name=}, {age=}")  # good for reporting, logging, debugging, etc.

song = "When an eel grabs your arm," \
       "And it causes great harm," \
       "That's a moray!"
print(song.replace("m", "M"))

fred = "Fred"
head = "head"
shit = "shit"
song2 = "My cat loves %s. My cat bites %s's %s. My cat thinks he's a %s."
print(song2 % (fred, fred, head, shit))
song3 = "My cat loves {fred}. My cat bites {fred}'s {head}. My cat thinks he's a {shit}.".format(fred=fred,
                                                                                                 head=head, shit=shit)
print(song3)
song4 = f"My cat loves {fred}. My cat bites {fred}'s {head}. My cat thinks he's a {shit}."
print(song4)

first_name = "Steven"
title = "CEO"
# tomorrow = time.strftime("%A")
email = f"""\nDear {first_name},
I hope my email finds you well this {time.strftime("%A")}.
I saw that you are the {title} and decided to reach out.
Hoping to see you soon."""
print(email)
