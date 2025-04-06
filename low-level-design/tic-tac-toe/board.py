from player import Player

class Board:
    def __init__(self):
        self.board = [['-' for i in range(3)] for j in range(3)]
        self.moves_done = 0
        self.rows = 3
        self.cols = 3

    def make_move(self, player: Player, row: int, col: int):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] != '-':
            raise ValueError('row/ col out of bound | cell is already taken')
        
        self.board[row][col] = player.symbol
        self.moves_done += 1

    def is_game_completed(self) -> bool:
        return self.moves_done >= 9
    
    def print_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.board[row][col])


    def has_winner(self):
        # Check Rows
        for row in range(self.rows):
            if self.board[row][0] != '-' and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return True
        # Check columns
        for col in range(3):
            if self.board[0][col] != '-' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True

        # Check diagonals
        if self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        return self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0]