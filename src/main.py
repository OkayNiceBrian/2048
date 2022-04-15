import sys
import pygame
from sqlalchemy import false
pygame.init()

size = width, height = 800, 800

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

leftPressed = False
rightPressed = False
upPressed = False
downPressed = False

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_UP:
                upPressed = False
            if event.key == pygame.K_DOWN:
                downPressed = False
        
    # Update
    speedConstant = clock.tick(60)
    
    # Draw
    black = 0, 0, 0
    screen.fill(black)
    pygame.display.flip()