#MAIN LOOP FOR TIC TAC TOE

import pygame
from pygame.locals import *

pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption = ('Tic-Tac-Toe')

def initBoard(ttt):
    
# initialize the board and return it
# as a variable
# ttt : a properly initialized display variable

    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250,250,250))

# draw the grid lines

# vertical lines...

    pygame.draw.line (background, (0,0,0), (100,0), (100,300), 2)
    pygame.draw.line (background, (0,0,0), (200,0), (200,300), 2)

# horizontal lines...

    pygame.draw.line (background, (0,0,0), (0,100), (300,100), 2)
    pygame.draw.line (background, (0,0,0), (0,200), (300,200), 2)

    return background
        
board = initBoard(ttt)

def showBoard (ttt, board):
# (re)draw the game board (board) on the screen (ttt)
    ttt.blit(board, (0,0))
    pygame.display.flip()

play = 1

while (play==1):
    for event in pygame.event.get():
        if event.type is QUIT:
            play = 0
    showBoard(ttt, board)
    

showBoard(ttt, board)
