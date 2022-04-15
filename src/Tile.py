import pygame

class Tile:
    w = 200
    h = 200
    
    def __init__(self, images):
        self.value = 0
        self.images = images
        self.image = images[0]
        
    def setValue(self, v):
        self.value = v
        self.image = self.images[self.value]
        
