def print_red(*s, end="\n"):
    print('\33[41m\33[30m', end="")
    for c in s:
        print(c, end="")
    print('\033[0m', end=end)


def print_yellow(*s, end="\n"):
    print('\33[103m\33[30m', end="")
    for c in s:
        print(c, end="")
    print('\033[0m', end=end)


def main():
    print_red("This is RED")
    print_yellow("This is YELLOW")
    for i in range(7):
        print("|", end="")

        c = "   "
        if i % 3 == 0:
            c = " * "

        if i % 2 == 0:
            print_red(c, end="")
        else:
            print_yellow(c, end="")

    print("|")


if __name__ == '__main__':
    main()
