from collections import defaultdict

from datetime import datetime, timedelta


def get_norm_weekday_user_birthday(birthday):
    weekday = birthday.weekday()
    if (weekday >= 5):
        birthday = birthday + timedelta(days=(7 - weekday))
    return birthday


def get_user_birthday_this_year(user_birthday, today):
    birthday = user_birthday.date()
    birthday_this_year = birthday.replace(year=today.year)
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    return birthday_this_year


def show(result):
    result_string = ''
    for day_name, names in result.items():
        names_string = ', '.join(names)
        result_string = result_string + f'{day_name}: {names_string}\n'
    print(result_string)


def main(users):
    result = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name, birthday = user.values()
        birthday_this_year = get_user_birthday_this_year(birthday, today)
        birthday_this_year = get_norm_weekday_user_birthday(birthday_this_year)
        delta_days = (birthday_this_year - today).days
        if delta_days > 7:
            continue
        result[birthday_this_year.strftime("%A")].append(name)
    show(result)
