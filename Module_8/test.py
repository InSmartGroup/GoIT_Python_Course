import itertools
from datetime import datetime, timedelta
from time import sleep, time
import timeit
import math
import collections

# # date and time manipulation
# current_date = datetime.now()
# print(current_date)  # year-month-day hh:mm:ss.milliseconds
# print(current_date.time())  # time, including milliseconds
# print(current_date.hour)  # hour
# print(current_date.minute)  # minute
# print(current_date.second)  # second
# print(current_date.year)  # year
# print(current_date.month)  # month
# print(current_date.day)  # day
#
# # time delta
# timeshift = timedelta(days=45)
# print(current_date + timeshift)
#q
# # timestamp
# print(current_date.timestamp())
#
# print(datetime.strptime('1970:01:01 January Jan 03 03 00', '%Y:%m:%d %B %b %H %I %M'))

# for i in range(30):
#     date = datetime.now()
#     sleep(1)
#     print(date.strftime('%H:%m:%S, %A'))

# print(math.pi)
# print(math.sqrt(pow(math.pi, 5)))
# print(math.sin(3) * math.cos(5))

# tempts = [3, 1, 1, 6, 7, 4, 5, 11, 9, 2, 6, 5, 10, 18, 7, 3, 7, 11, 13, 6, 6, 1, 19, 6]
# counter = collections.Counter(tempts)
# print(counter)
# print(counter.most_common(1))
#
# new_counter = [[f"number: {i}", f"count: {tempts.count(i)}"] for i in tempts]
# print(new_counter)

# lst = [i for i in range(10)]
# my_q = collections.deque(lst)
# print(my_q)

# # program execution time
# start = time()
# sleep(1)
# print('hello')
# print('world')
# print('my name is Greg')
# print(time() - start)
