from Tile import Tile
import random
import pygame

class Board:
    w = 800
    h = 800
    
    def __init__(self, images):
        self.images = images
        self.boardState = []
        self.resetBoard()
        
    def draw(self, screen):
        for i in range(self.boardState.__len__()):
            for j in range(self.boardState[i].__len__()):
                tile = self.boardState[i][j]
                rect = tile.image.get_rect(topleft=(j * Tile.w, i * Tile.h))
                screen.blit(tile.image, rect)
        
    def resetBoard(self):
        board = [
            [Tile(self.images), Tile(self.images), Tile(self.images), Tile(self.images)],
            [Tile(self.images), Tile(self.images), Tile(self.images), Tile(self.images)],
            [Tile(self.images), Tile(self.images), Tile(self.images), Tile(self.images)],
            [Tile(self.images), Tile(self.images), Tile(self.images), Tile(self.images)]
        ]
        
        x1 = random.randint(0, 3)
        y1 = random.randint(0, 3)
        
        x2 = random.randint(0, 3)
        y2 = random.randint(0, 3)
        
        while (x1 == x2 and y1 == y2):
            x2 = random.randint(0, 3)
            y2 = random.randint(0, 3)
            
        board[x1][y1].setValue(2)
        board[x2][y2].setValue(2)
        
        self.boardState = board
        
        