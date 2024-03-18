import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generate_mines()

    # Define other methods as in the previous code...

    def game_over(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()

def main():
    rows = 10
    cols = 10
    mines = 10

    game = Minesweeper(rows, cols, mines)
    game.game_over()

if __name__ == "__main__":
    main()
