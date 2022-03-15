import pygame
from pygame.locals import * 

# GRID
BOARDWINDOWWIDTH = 675
BOARDWINDOWHEIGHT = 675

# COLOR
BLOCKCOLOR = (245,0,124)

class Grid:

    def __init__(self):
        self.reset()

    def reset(self):
        self.block_size = 50
        self.rects = []
        self.rectsColors = []
        self.width = []

        for y in range(225, BOARDWINDOWWIDTH, self.block_size):
            for x in range(225, BOARDWINDOWHEIGHT, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                self.rects.append(rect)
                self.rectsColors.append(BLOCKCOLOR)
                self.width.append(1)

    
    def display(self, game_window):
        index = 0
        for r in self.rects:
            pygame.draw.rect(game_window, self.rectsColors[index], r, self.width[index])
            index += 1 