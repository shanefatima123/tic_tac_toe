from game.board import Board
from game.players import Player
from game.utils import MoveHandler
from tools.logger import Logger  # Importing the Logger class

# Modularized functions
def welcome_message(p1, p2):
    print(f"\nWelcome, {p1} and {p2}!\n")

def print_board(board):
    # Display the current state of the board
    for i in range(3):
        print(" | ".join(str(board[i][j]) for j in range(3)))
        if i < 2:
            print("-----------")

def announce_winner(name):
    print(f"\nCongratulations, {name}! You win!\n")

def announce_draw():
    print("\nIt's a draw!\n")

def main():
    print("Welcome to Tic-Tac-Toe!")

    # Get player names
    player1_name = input("Please enter Player 1 name: ")
    player2_name = input("Please enter Player 2 name: ")

    welcome_message(player1_name, player2_name)

    # Initialize the logger
    logger = Logger()  # Initialize logger here

    # Main game loop
    while True:
        board = Board()
        player1 = Player(player1_name, "X")
        player2 = Player(player2_name, "O")
        current_player = player1

        logger.log_game_start(player1, player2)  # Log game start

        move_num = 1  # Track the number of moves

        while not board.is_full():
            print_board(board.grid)

            print(f"\n{current_player.name}'s Turn ({current_player.marker}):")
            move = MoveHandler.get_move(current_player.name, board.grid)

            row, col = move  # Convert 1-9 move to (row, col)
            if board.make_move(row, col, current_player.marker):
                # Log the move with the current board display
                logger.log_move(move_num, current_player, (row * 3 + col + 1), board)  # Log the move
                move_num += 1

                if board.check_winner(current_player.marker):
                    print_board(board.grid)
                    announce_winner(current_player.name)
                    logger.log_result(f"{current_player.name} wins")  # Log the result
                    break

                # Switch to the next player
                current_player = player2 if current_player == player1 else player1
            else:
                print("Invalid move. Try again.")

        else:
            print_board(board.grid)
            announce_draw()
            logger.log_result("Draw")  # Log the result for a draw

        # Ask if they want to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
