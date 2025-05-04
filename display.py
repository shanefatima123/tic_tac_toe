def welcome_message(p1, p2):
    print(f"\nWelcome, {p1} and {p2}!\n")

def print_board(board):
    print(board.display())

def announce_winner(name):
    print(f"\nCongratulations, {name}! You win!\n")

def announce_draw():
    print("\nIt's a draw!\n")

def prompt_restart():
    return input("Would you like to play again? (yes/no): ").strip().lower().startswith('y')

