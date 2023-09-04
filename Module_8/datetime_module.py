from datetime import datetime as dt
import time

date_now = dt.now()
# print(date_now.date())
# print(date_now.strftime('%D'))  # common date format
# print(date_now.strftime('%A'))  # day, full
# print(date_now.strftime('%a'))  # day, short
# print(date_now.strftime('%d'))  # day, digit
# print(date_now.strftime('%Y'))  # year
# print(date_now.strftime('%B'))  # month, full
# print(date_now.strftime('%b'))  # month, short
# print(date_now.strftime('%m'))  # month, digit
# print(date_now.strftime('%H'))  # hour
# print(date_now.strftime('%M'))  # minute
# print(date_now.strftime('%S'))  # second

# date_ts = dt(year=1986, month=11, day=15, hour=23, minute=17, second=41)
# print(date_ts.strftime('%Y %B, %A %dth, %H:%M:%S'))  # custom datetime object formatting
# print(dt.strptime('1986 November, Saturday 15th, 23:17:41', '%Y %B, %A %dth, %H:%M:%S'))  # from string to datetime
# print(date_ts.timestamp())  # datetime object to timestamp
# print(dt.fromtimestamp(532473461.0))  # from timestamp to datetime object

# start = time.time()
# my_list = [i for i in range(100000000)]  # it takes 8.205958604812622 seconds to perform this operation
# end = time.time()
# print(end-start)  # calculate the duration of an operation

date_bd = dt(year=2013, month=5, day=24, hour=19, minute=30)
print(date_bd.strftime("My daughter was born in %Y, %b %dth at %H:%M. It was %A."))
difference_days = date_now.date() - date_bd.date()
print(f"It was {difference_days.days} days ago. I remember that day very well.")
difference_years = date_now.year - date_bd.year
print(f"Now she is {difference_years} years old. I love her so much!")
