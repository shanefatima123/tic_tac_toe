from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent / "game_log"
        self.game_id = self.get_next_game_id()
        self.log_dir = self.base_path / f"game{self.game_id}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "log.txt"
        self.moves = []

    def get_next_game_id(self):
        self.base_path.mkdir(parents=True, exist_ok=True)
        return len([f for f in self.base_path.iterdir() if f.is_dir()]) + 1

    def log_game_start(self, p1, p2):
        with self.log_file.open('w') as f:
          f.write(f"Game {self.game_id} Log\n\nPlayers:\n- {p1.name} ({p1.marker})\n- {p2.name} ({p2.marker})\n\n")


    def log_move(self, move_num, player, position, board):
        entry = f"Move {move_num}: {player.name} -> Position {position}\n"
        entry += "Board After Move:\n" + board.display() + "\n"
        with self.log_file.open('a') as f:
            f.write(entry)

    def log_result(self, result):
        with self.log_file.open('a') as f:
            f.write(f"Result: {result}\n")

