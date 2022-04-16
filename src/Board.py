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
        
    def up(self):
        # DOESN'T WORK
        print("up")
        new2 = random.randint(0, self.boardState.__len__() - 1)
        
        invertedBoardState = self.boardState.copy()
        for i in range(self.boardState.__len__()):
            for j in range(self.boardState[i].__len__()):
                invertedBoardState[j][i].setValue(self.boardState[i][j].value)
                
        for i in range(self.boardState.__len__()):
            print(self.boardState[i][0].__str__() + " " + self.boardState[i][1].__str__() + " " + self.boardState[i][2].__str__() + " " + self.boardState[i][3].__str__())
        print("================")
        for i in range(invertedBoardState.__len__()):
            print(invertedBoardState[i][0].__str__() + " " + invertedBoardState[i][1].__str__() + " " + invertedBoardState[i][2].__str__() + " " + invertedBoardState[i][3].__str__())
        
        for i in range(invertedBoardState.__len__()):
            row = invertedBoardState[i]
            j = 1
            checking = True
            while (j < row.__len__()):
                if checking:
                    if row[j].value == row[j - 1].value or row[j - 1].value == 0 or row[j].value == 0:
                        row[j - 1].setValue(row[j].value + row[j - 1].value)
                        checking = False
                else:
                    row[j - 1].setValue(row[j].value)
                j += 1 
            
            if not checking:
                if i == new2:
                    row[row.__len__() - 1].setValue(2)
                else:
                    row[row.__len__() - 1].setValue(0)

            invertedBoardState[i] = row
        
        for i in range(self.boardState.__len__()):
            for j in range(self.boardState[i].__len__()):
                self.boardState[i][j].setValue(invertedBoardState[j][i].value)
        
    def down(self):
        print("down")
        new2 = random.randint(0, self.boardState.__len__() - 1)
        
    def left(self):
        print("left")
        new2 = random.randint(0, self.boardState.__len__() - 1)
        for i in range(self.boardState.__len__()):
            row = self.boardState[i]
            j = 1
            checking = True
            while (j < row.__len__()):
                if checking:
                    if row[j].value == row[j - 1].value or row[j - 1].value == 0 or row[j].value == 0:
                        row[j - 1].setValue(row[j].value + row[j - 1].value)
                        checking = False
                else:
                    row[j - 1].setValue(row[j].value)
                j += 1 
            
            if not checking:
                if i == new2:
                    row[row.__len__() - 1].setValue(2)
                else:
                    row[row.__len__() - 1].setValue(0)

            self.boardState[i] = row
            
    def right(self):
        print("right")
        new2 = random.randint(0, self.boardState.__len__() -2)
        for i in range(self.boardState.__len__()):
            row = self.boardState[i]
            j = row.__len__() - 2
            checking = True
            while (j >= 0):
                if checking:
                    if row[j].value == row[j + 1].value or row[j + 1].value == 0 or row[j].value == 0:
                        row[j + 1].setValue(row[j].value + row[j + 1].value)
                        checking = False
                else:
                    row[j + 1].setValue(row[j].value)
                j -= 1
            
            if not checking:
                if i == new2:
                    row[0].setValue(2)
                else:
                    row[0].setValue(0)

            self.boardState[i] = row
            
        
        