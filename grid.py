import pygame
from pygame.locals import * 

# GRID
BOARDWINDOWWIDTH = 675
BOARDWINDOWHEIGHT = 675

# COLOR
BLOCKCOLOR = (220,220,220)

class Grid:
    def __init__(self):
        self.block_size = 50
    
    def display(self, game_window):
        for x in range(225, BOARDWINDOWWIDTH, self.block_size):
            for y in range(225, BOARDWINDOWHEIGHT, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(game_window, BLOCKCOLOR, rect, 1)