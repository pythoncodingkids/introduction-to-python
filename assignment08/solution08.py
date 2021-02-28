def read_file(file_name):
    content = []
    with open(file_name, 'r') as f:
        for line in f:
            line_list = list(line.strip())
            if len(line_list) > 0:
                content.append(line_list)
    return content


def start_character_same(word, puzzle, row, col):
    return word[0] == puzzle[row][col]


def word_can_fit_right(word, col, puzzle_width):
    return len(word) <= (puzzle_width - col)


def word_can_fit_left(word, col):
    return len(word) <= (col + 1)


def word_can_fit_below(word, row, puzzle_height):
    return len(word) <= (puzzle_height - row)


def word_can_fit_above(word, row):
    return len(word) <= (row + 1)


def word_match_right(word, puzzle, row, col):
    puzzle_characters = puzzle[row][col:(col + len(word))]
    return word == puzzle_characters


def reverse(word):
    reversed_word = []
    for i in range(len(word)-1, -1, -1):
        reversed_word.append(word[i])
    return reversed_word


def word_match_left(word, puzzle, row, col):
    puzzle_characters = puzzle[row][((col + 1) - len(word)):(col + 1)]
    return word == reverse(puzzle_characters)


def word_match_below(word, puzzle, row, col):
    puzzle_characters = []
    for r in range(row, (row + len(word))):
        puzzle_characters.append(puzzle[r][col])
    return word == puzzle_characters


def word_match_above(word, puzzle, row, col):
    puzzle_characters = []
    for r in range(row, row - len(word), -1):
        puzzle_characters.append(puzzle[r][col])
    return word == puzzle_characters


def word_match_diagonally_right_below(word, puzzle, row, col):
    puzzle_characters = []
    shift = 0
    for r in range(row, (row + len(word))):
        puzzle_characters.append(puzzle[r][(col + shift)])
        shift += 1
    return word == puzzle_characters


def word_match_diagonally_left_below(word, puzzle, row, col):
    puzzle_characters = []
    shift = 0
    for r in range(row, (row + len(word))):
        puzzle_characters.append(puzzle[r][(col - shift)])
        shift += 1
    return word == puzzle_characters


def word_match_diagonally_right_above(word, puzzle, row, col):
    puzzle_characters = []
    shift = 0
    for r in range(row, (row - len(word)), -1):
        puzzle_characters.append(puzzle[r][(col + shift)])
        shift += 1
    return word == puzzle_characters


def word_match_diagonally_left_above(word, puzzle, row, col):
    puzzle_characters = []
    shift = 0
    for r in range(row, (row - len(word)), -1):
        puzzle_characters.append(puzzle[r][(col - shift)])
        shift += 1
    return word == puzzle_characters


def word_exists(word, puzzle, row, col, puzzle_width, puzzle_height):
    if start_character_same(word, puzzle, row, col):
        fit_right = word_can_fit_right(word, col, puzzle_width)
        fit_left = word_can_fit_left(word, col)
        fit_below = word_can_fit_below(word, row, puzzle_height)
        fit_above = word_can_fit_above(word, row)
        if fit_right and word_match_right(word, puzzle, row, col):
            return True, 'Right'
        elif fit_left and word_match_left(word, puzzle, row, col):
            return True, 'Left'
        elif fit_below and word_match_below(word, puzzle, row, col):
            return True, 'Below'
        elif fit_above and word_match_above(word, puzzle, row, col):
            return True, 'Above'
        elif fit_right and fit_below and word_match_diagonally_right_below(word, puzzle, row, col):
            return True, 'Diagonally Right Below'
        elif fit_right and fit_above and word_match_diagonally_right_above(word, puzzle, row, col):
            return True, 'Diagonally Right Above'
        elif fit_left and fit_below and word_match_diagonally_left_below(word, puzzle, row, col):
            return True, 'Diagonally Left Below'
        elif fit_left and fit_above and word_match_diagonally_left_above(word, puzzle, row, col):
            return True, 'Diagonally Left Above'
        else:
            return False, ''
    else:
        return False, ''


def print_puzzle(puzzle):
    print("PUZZLE")
    print("------")
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            print(puzzle[r][c], " ", end="")
        print()


def main():
    puzzle_file_name = input("Please enter puzzle file name: ")
    puzzle = read_file(puzzle_file_name)
    words_file_name = input("Please enter words file name: ")
    words = read_file(words_file_name)
    puzzle_width = len(puzzle[0])
    puzzle_height = len(puzzle)

    print_puzzle(puzzle)

    print("SOLUTION")
    print("--------")
    for word in words:
        for row in range(puzzle_height):
            word_found = False
            for col in range(puzzle_width):
                result = word_exists(word, puzzle, row, col, puzzle_width, puzzle_height)
                if result[0]:
                    print("".join(word), "exists", result[1], ("from (" + str(row) + ", " + str(col) + ")"))
                    word_found = True
                    break
            if word_found:
                break


if __name__ == '__main__':
    main()
