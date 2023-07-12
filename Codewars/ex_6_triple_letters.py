# Create a function that returns one string out of the three input strings
# Taking the first letter of all of the inputs and grouping them next to each other
# Do this for every letter
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

def triple_trouble(one, two, three):
    new_str = ""
    for a, b, c in zip(one, two, three):
        new_str += a + b + c

    return new_str


print(triple_trouble('aa', 'bb', 'cc'))
