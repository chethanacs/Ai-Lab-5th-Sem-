import math

board = [" "] * 9


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please choose a number from 1 to 9.")
            elif board[move] != " ":
                print("That position is already taken.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Enter a valid number.")


def main():
    print("=== TIC-TAC-TOE ===")
    print("You are X. Computer is O.")

    while True:
        print_board()

        player_move()

        result = check_winner()
        if result:
            print_board()
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        computer_move()

        result = check_winner()
        if result:
            print_board()
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break


if __name__ == "__main__":
    main()
