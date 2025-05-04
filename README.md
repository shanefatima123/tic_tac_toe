# 🎮 Tic-Tac-Toe (Python Terminal Game)

This is a modular, terminal-based Tic-Tac-Toe game written in Python. It allows two players to play alternately, logs each move into a file, and supports replaying multiple games in a session.

---

## 📁 Project Structure

tic_tac_toe/
│
├── game/
│ ├── board.py # Handles the game board logic
│ ├── players.py # Defines the Player class
│ └── utils.py # Move handling utility
│
├── tools/
│ └── logger.py # Logger for game history (game start, moves, results)
│
├── logs/
│ └── game_log_<id>.txt # Log files for each game
│
├── main.py # Entry point to start the game
└── README.md # Project documentation
