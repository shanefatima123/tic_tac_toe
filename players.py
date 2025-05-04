import random

class Player:
    def __init__(self, name, marker, is_computer=False):
        self.name = name
        self.marker = marker
        self.is_computer = is_computer

    def get_move(self, available_moves):
        if self.is_computer:
            return random.choice(available_moves)
        while True:
            try:
                move = int(input(f"{self.name}'s Turn ({self.marker}): Enter position (1-9): "))
                if move in available_moves:
                    return move
                print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number.")
