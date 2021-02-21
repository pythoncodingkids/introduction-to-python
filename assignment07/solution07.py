def get_addition_matrix_dimension():
    dimension_string = input("Enter matrix dimension (ex. 2x3): ")
    dimension_string_list = dimension_string.split("x")
    rows = int(dimension_string_list[0].strip())
    cols = int(dimension_string_list[1].strip())
    return rows, cols


def get_multiply_matrix_dimension():
    dimension_correct = False
    row1 = col1 = row2 = col2 = 0
    while not dimension_correct:
        dimension_string = input("Enter matrix dimensions (ex. 2x3, 3x2): ")
        dimension_string_list = dimension_string.split(",")
        first_matrix_dimension_list = dimension_string_list[0].split("x")
        row1 = int(first_matrix_dimension_list[0].strip())
        col1 = int(first_matrix_dimension_list[1].strip())
        second_matrix_dimension_list = dimension_string_list[1].split("x")
        row2 = int(second_matrix_dimension_list[0].strip())
        col2 = int(second_matrix_dimension_list[1].strip())
        if col1 != row2:
            print("First matrix columns must be equal to second matrix rows!")
        else:
            dimension_correct = True
    return row1, col1, row2, col2


def get_matrix(rows, columns, label=None):
    matrix = []
    print("Enter", label, "matrix values (values separated by space, rows entered in new lines)")
    for r in range(rows):
        row_string = input()
        row_string_list = row_string.split()
        while len(row_string_list) != columns:
            print("Invalid number of columns, columns must be " + str(columns) + ", enter row again")
            row_string = input()
            row_string_list = row_string.split()
        row = []
        for v in row_string_list:
            row.append(int(v.strip()))
        matrix.append(row)
    return matrix


def add_matrix(a, b):
    result = []
    for r in range(len(a)):
        added_row = []
        for c in range(len(a[0])):
            added_row.append(a[r][c] + b[r][c])
        result.append(added_row)
    return result


def get_column(m, index):
    column = []
    for row in m:
        column.append(row[index])
    return column


def multiply_matrix(a, b):
    result = []
    for row_index in range(len(a)):
        row = a[row_index]
        new_row = []
        for col_index in range(len(b[0])):
            column = get_column(b, col_index)
            total = 0
            for i in range(len(row)):
                total += row[i] * column[i]
            new_row.append(total)
        result.append(new_row)
    return result


def print_matrix(matrix):
    for r in matrix:
        row = []
        for c in r:
            row.append(str(c))
        print(" ".join(row))


def main():
    while True:
        add_or_multiply = input("Enter a => to add, m => to multiple: ")
        if add_or_multiply == "a":
            rows, columns = get_addition_matrix_dimension()
            first = get_matrix(rows, columns, "first")
            second = get_matrix(rows, columns, "second")
            result = add_matrix(first, second)
            print("Result: ")
            print_matrix(result)
            print()
        elif add_or_multiply == "m":
            row1, column1, row2, column2 = get_multiply_matrix_dimension()
            first = get_matrix(row1, column1, "first")
            second = get_matrix(row2, column2, "second")
            result = multiply_matrix(first, second)
            print("Result: ")
            print_matrix(result)
            print()
        else:
            print("Invalid command")


if __name__ == '__main__':
    main()
