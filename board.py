class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        lines = []
        for i in range(3):
            row = " | ".join(str(self.grid[i][j]) for j in range(3))
            lines.append(row)
            if i < 2:
                lines.append("-----------")
        return "\n".join(lines)  # Ensure this always returns a string

    def make_move(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True

        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)
