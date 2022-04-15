import sys
import pygame
from Board import Board

pygame.init()
size = width, height = 800, 800

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

leftPressed = False
rightPressed = False
upPressed = False
downPressed = False
spacePressed = False

images = {
    0: pygame.image.load("../assets/0-tile.png"),
    2: pygame.image.load("../assets/2-tile.png"),
    4: pygame.image.load("../assets/4-tile.png"),
    8: pygame.image.load("../assets/8-tile.png"),
    16: pygame.image.load("../assets/16-tile.png"),
    32: pygame.image.load("../assets/32-tile.png"),
    64: pygame.image.load("../assets/64-tile.png"),
    128: pygame.image.load("../assets/128-tile.png"),
    256: pygame.image.load("../assets/256-tile.png"),
    512: pygame.image.load("../assets/512-tile.png"),
    1024: pygame.image.load("../assets/1024-tile.png"),
    2048: pygame.image.load("../assets/2048-tile.png")
}

board = Board(images)

while 1:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftPressed = True
            if event.key == pygame.K_RIGHT:
                rightPressed = True
            if event.key == pygame.K_UP:
                upPressed = True
            if event.key == pygame.K_DOWN:
                downPressed = True
            if event.key == pygame.K_SPACE:
                spacePressed = True
                board.resetBoard()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_UP:
                upPressed = False
            if event.key == pygame.K_DOWN:
                downPressed = False
            if event.key == pygame.K_SPACE:
                spacePressed = False
        
    # Update
    speedConstant = clock.tick(60)
    
    # Draw
    black = 0, 0, 0
    screen.fill(black)
    board.draw(screen)
    pygame.display.flip()