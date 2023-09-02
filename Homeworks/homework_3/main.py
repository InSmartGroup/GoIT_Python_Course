from datetime import datetime


def get_birthdays_per_week(users: list):
    """
    Returns a dictionary of names of people that have a birthday within the following 7 days.
    
    :param users: A list of dictionaries that specify a person's 'name' and 'birthday'.
    The 'birthday' key must store a datetime.date() object.
    :type users: list
    
    :return: A list of names.
    :rtype: dict
    """
    # a dictionary to store the end result
    users_to_congratulate = {'Monday': [],
                             'Tuesday': [],
                             'Wednesday': [],
                             'Thursday': [],
                             'Friday': []}

    # retrieve the info from the current date
    current_date = datetime.today().date()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day

    if len(users) > 0:
        for user in users:
            # retrieve the info from user's birthdate
            user_name = user['name']
            user_birthdate = user['birthday']
            user_birthyear = user_birthdate.year
            user_birthmonth = user_birthdate.month
            user_birthday = user_birthdate.day
            user_birthday_weekday = user_birthdate.strftime("%A")

            # check if the user was born on weekend and move his birthday to Monday
            if user_birthday_weekday == 'Saturday' or user_birthday_weekday == 'Sunday':
                user_birthday_weekday = 'Monday'

            # check if the user's birthday will occur in the following 7 days
            if user_birthyear <= current_year:
                if user_birthmonth == current_month:
                    if user_birthday - current_day <= 7:
                        users_to_congratulate[user_birthday_weekday].append(user_name)
            else:
                print(f"A person named {user_name} is not born yet. Please check the date.")

        # this cleans the initial list in case it's empty to return only non-empty items
        clean_welcome_list = {}
        for k, v in users_to_congratulate.items():
            if v:
                clean_welcome_list[k] = v

        return clean_welcome_list

    else:
        return 'Your list must contain dictionaries and shouldn\'t be empty'


if __name__ == '__main__':
    # test dictionaries
    birthdays = [{"name": "Bill", "birthday": datetime(1986, 9, 2).date()},
                 {"name": "John", "birthday": datetime(1986, 9, 4).date()},
                 {"name": "Steve", "birthday": datetime(1986, 10, 2).date()},
                 {"name": "Jeniffer", "birthday": datetime(1986, 12, 1).date()},
                 {"name": "Gregory", "birthday": datetime(2024, 1, 14).date()},
                 {"name": "William", "birthday": datetime(1986, 11, 28).date()},
                 {"name": "Carla", "birthday": datetime(1986, 9, 9).date()}]

    birthdays_2 = []

    print(get_birthdays_per_week(birthdays))
