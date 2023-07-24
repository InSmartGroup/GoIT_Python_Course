"""
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
For example n = 3 result in:
"I\n I\n  I"

or printed:
I
 I
  I
"""


def draw_stairs(n):
    lst = []

    for i in range(1, n + 1):
        item = "I\n" + " " * i
        lst.append(item)

    lst[-1] = "I"

    return "".join(lst)


print(draw_stairs(3))
print(draw_stairs(7))
print(draw_stairs(11))
