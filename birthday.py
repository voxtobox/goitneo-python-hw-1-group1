from collections import defaultdict

from datetime import datetime, timedelta


def main(users):
    result = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days > 7:
            continue
        if (birthday_this_year.weekday() >= 5):
            birthday_this_year = birthday_this_year + \
                timedelta(days=7 - birthday_this_year.weekday())

        result[birthday_this_year.strftime("%A")].append(name)
    result_string = ''
    for day_name, names in result.items():
        names_string = ', '.join(names)
        result_string = result_string + f'{day_name}: {names_string}\n'
    print(result_string)


if __name__ == "__main__":
    main()
