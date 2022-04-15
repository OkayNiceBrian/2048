import Tile
import random

class Board:
    w = 800
    h = 800
    
    def __init__(self):
        self.boardState = Board.setupBoard()
        
    def resetBoard(self):
        self.boardState = Board.setupBoard()
        
    @staticmethod
    def setupBoard():
        board = [
            [Tile(), Tile(), Tile(), Tile()],
            [Tile(), Tile(), Tile(), Tile()],
            [Tile(), Tile(), Tile(), Tile()],
            [Tile(), Tile(), Tile(), Tile()]
        ]
        
        x1 = random.randint(0, 3)
        y1 = random.randint(0, 3)
        
        x2 = random.randint(0, 3)
        y2 = random.randint(0, 3)
        
        while (x1 == x2 and y1 == y2):
            x2 = random.randint(0, 3)
            y2 = random.randint(0, 3)
            
        board[x1][y1] = 2
        board[x2][y2] = 2
        
        return board
        
        