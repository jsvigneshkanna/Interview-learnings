from player import Player
from board import Board

class TicTacToeGame:
    _instance: None

    def __init__(self, player1: Player, player2: Player, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = board

    # def get_instance(cls):
    #     if not cls._instance:
    #         cls._instance = TicTacToeGame()
    #     return cls._instance
    
    def play(self):
        while not self.board.is_game_completed() and not self.board.has_winner():
            print(f"{self.current_player.get_name()}'s turn.")
            row = self.get_valid_input("Enter row (0-2): ")
            col = self.get_valid_input("Enter column (0-2): ")
            try:
                self.board.make_move(self.current_player, row, col)
                self.board.print_board()
                self.switch_player()
            except ValueError as e:
                print(str(e))

        if self.board.has_winner():
            self.switch_player()
            print(f"{self.current_player.get_name()} wins!")
        else:
            print("It's a draw!")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def get_valid_input(self, message):
        while True:
            try:
                user_input = int(input(message))
                if 0 <= user_input <= 2:
                    return user_input
                else:
                    print("Invalid input! Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 2.")