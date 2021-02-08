def initialize_board():
    board = [["1", "4", "7"],
             ["2", "5", "8"],
             ["3", "6", "9"]]
    return board


def print_board(board):
    print("-------")
    for y in range(0, 3):
        print("|", end="")
        for x in range(0, 3):
            print(board[x][y] + "|", end="")
        print()
    print("-------")


def translate_position_to_coordinate(position):
    return (position - 1) % 3, (position - 1) // 3


def mark_board(board, position, mark):
    x, y = translate_position_to_coordinate(position)
    board[x][y] = mark


def is_position_taken(board, position):
    x, y = translate_position_to_coordinate(position)
    mark = board[x][y]
    if mark == 'x' or mark == 'o':
        return True
    else:
        return False


def check_if_player_won(board, player):
    # check rows
    for y in range(0, 3):
        if board[0][y] == player and board[1][y] == player and board[2][y] == player:
            return True

    # check columns
    for x in range(0, 3):
        if board[x][0] == player and board[x][1] == player and board[x][2] == player:
            return True

    # check diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_if_draw(board):
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] != 'x' and board[x][y] != 'o':
                return False

    return True


def switch_player(player):
    if player == "x":
        return "o"
    else:
        return "x"


def main():
    play = True
    start_player = "x"
    player = start_player

    board = initialize_board()
    print_board(board)

    while play:
        position = int(input("It's " + player+"'s turn, choose position: "))
        if is_position_taken(board, position):
            print("Position", position, "already taken!")
        else:
            mark_board(board, position, player)
            print_board(board)

            game_finished = False
            if check_if_player_won(board, player):
                print(player, "won !!!")
                game_finished = True
            elif check_if_draw(board):
                print("It is a draw !")
                game_finished = True

            if game_finished:
                print()
                cmd = int(input("Do you want to play again? 1 to continue, 0 to exit: "))
                if cmd == 0:
                    play = False
                else:
                    board = initialize_board()
                    print_board(board)
                    start_player = switch_player(start_player)
                    player = start_player
            else:
                player = switch_player(player)


if __name__ == '__main__':
    main()
