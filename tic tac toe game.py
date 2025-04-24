# Tic Tac Toe game

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw():
    return ' ' not in board

def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move, please try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")

def main():
    current_player = 'X'
    while True:
        print_board()
        player_move(current_player)
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
