# Create a function that accepts a string and a single character
# and returns an integer of the count of occurrences the 2nd argument is found in the first one
# If no occurrences can be found, a count of 0 should be returned

def str_count(strng, letter):
    if letter in strng:
        return strng.count(letter)
    else:
        return 0


print(str_count("Hello there, my dear friend", "e"))
print(str_count("I hope you all had a blessed and happy day", "a"))
