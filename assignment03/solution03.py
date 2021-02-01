NUM_OF_DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def is_same_year(year1, year2):
    return year1 == year2


def is_same_month(month1, month2):
    return month1 == month2


def get_num_of_days_in_month(year, month):
    if is_leap_year(year) and month == 2:
        return NUM_OF_DAYS_IN_MONTH[month - 1] + 1
    else:
        return NUM_OF_DAYS_IN_MONTH[month - 1]


def get_num_of_days_in_year(year):
    days = 0
    for month in range(1, 13):
        days = days + get_num_of_days_in_month(year, month)
    return days


def get_remainder_of_days_in_month(year, month, day):
    days_in_month = get_num_of_days_in_month(year, month)
    return days_in_month - day


def get_remainder_of_days_in_year(year, month, day):
    days = 0
    for m in range(month, 13):
        if m == month:
            days = days + get_remainder_of_days_in_month(year, month, day)
        else:
            days = days + get_num_of_days_in_month(year, m)
    return days


def get_past_days_in_year(year, month, day):
    days = 0
    for m in range(1, month+1):
        if m == month:
            days = days + day
        else:
            days = days + get_num_of_days_in_month(year, m)
    return days


def calc_num_of_days_in_between(from_year, from_month, from_day, to_year, to_month, to_day):
    if is_same_year(from_year, to_year) and is_same_month(from_month, to_month):
        return to_day - from_day
    elif is_same_year(from_year, to_year):
        days = 0
        for month in range(from_month, to_month + 1):
            if month == from_month:
                days = days + get_remainder_of_days_in_month(from_year, from_month, from_day)
            elif month == to_month:
                days = days + to_day
            else:
                days = days + get_num_of_days_in_month(from_year, month)
        return days
    else:
        days = 0
        for year in range(from_year, to_year + 1):
            if year == from_year:
                days = days + get_remainder_of_days_in_year(from_year, from_month, from_day)
            elif year == to_year:
                days = days + get_past_days_in_year(to_year, to_month, to_day)
            else:
                days = days + get_num_of_days_in_year(year)
        return days


def main():
    while True:
        from_year = int(input("from year: "))
        from_month = int(input("from month: "))
        from_day = int(input("from day: "))
        to_year = int(input("to year: "))
        to_month = int(input("to month: "))
        to_day = int(input("to day: "))
        print("Number of days between the above two date is:",
              calc_num_of_days_in_between(from_year, from_month, from_day, to_year, to_month, to_day))
        print()


if __name__ == '__main__':
    main()
