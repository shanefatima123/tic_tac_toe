# File: game/utils.py

class MoveHandler:
    @staticmethod
    def get_move(player_name, board):
        while True:
            try:
                move = input(f"{player_name}, enter your move as row and column (e.g., 0 2): ")
                row, col = map(int, move.strip().split())

                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates. Row and column must be between 0 and 2.")
                    continue
                if board[row][col] != " ":
                    print("That position is already taken. Try again.")
                    continue
                return row, col
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
