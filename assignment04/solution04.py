def minutes_in_between(start_hour, start_minute, end_hour, end_minute):
    if start_hour == end_hour and end_minute >= start_minute:
        minutes = end_minute - start_minute
    elif start_hour < end_hour:
        minutes = (60 - start_minute) + end_minute
        minutes += (end_hour - (start_hour + 1)) * 60
    else:
        minutes = (24 * 60) - minutes_in_between(end_hour, end_minute, start_hour, start_minute)

    return minutes


def fibonacci(n):
    n1 = 0
    n2 = 1
    fib = []
    for i in range(1, n+1):
        if i == 1:
            fib.append(n1)
        elif i == 2:
            fib.append(n2)
        else:
            n = n1 + n2
            fib.append(n)
            n1 = n2
            n2 = n
    return fib


def find_max_min_difference(list_of_num):
    def minimum(a, b):
        if a < b:
            return a
        else:
            return b

    def maximum(a, b):
        if a > b:
            return a
        else:
            return b

    max_value = list_of_num[0]
    min_value = list_of_num[0]
    for i in list_of_num:
        max_value = maximum(max_value, i)
    for i in list_of_num:
        min_value = minimum(min_value, i)

    return max_value - min_value


def less_than(list_of_num, limit):
    less_than_limit = []
    for i in list_of_num:
        if i < limit:
            less_than_limit.append(i)
    return less_than_limit


def reverse_list(list_of_num):
    reversed_list = []
    for i in range(len(list_of_num)-1, -1, -1):
        reversed_list.append(list_of_num[i])
    return reversed_list


def shift_list_by_1(list_of_num):
    shifted_list = []
    last_index = len(list_of_num)-1
    shifted_list.append(list_of_num[last_index])
    for i in range(0, last_index):
        shifted_list.append(list_of_num[i])
    return shifted_list


def shift_list(list_of_num, shift_by):
    shifted_list = []
    length = len(list_of_num)
    shift_by = shift_by % length
    from_index = length - shift_by
    for i in range(from_index, length):
        shifted_list.append(list_of_num[i])
    for i in range(0, from_index):
        shifted_list.append(list_of_num[i])
    return shifted_list


def nth_odd_number(list_of_num, n):
    num_of_odd_numbers = 0
    for i in list_of_num:
        if i % 2 == 1:
            num_of_odd_numbers += 1
        if num_of_odd_numbers == n:
            return i


def line_values(m, b, x_min, x_max):
    values = []
    for x in range(x_min, x_max+1):
        values.append(m*x + b)
    return values


def non_duplicates(list_of_num):
    def frequency(v):
        occurrence = 0
        for i in list_of_num:
            if i == v:
                occurrence += 1
        return occurrence

    non_duplicate_list = []
    for n in list_of_num:
        if frequency(n) == 1:
            non_duplicate_list.append(n)

    return non_duplicate_list










