from game import TicTacToeGame
from player import Player
from board import Board

def test_tictactoe():
    player1 = Player("Player 1", 'X')
    player2 = Player("Player 2", 'O')
    board = Board()
    game = TicTacToeGame(player1, player2, board)
    game.play()

if __name__ == '__main__':
    test_tictactoe()