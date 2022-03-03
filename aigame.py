import pygame
from pygame.locals import * 

BOARDWINDOWWIDTH = 675
BOARDWINDOWHEIGHT = 675

WINDOWWIDTH = 900
WINDOWHEIGHT = 900

BLOCKCOLORFILLWHITE = (250, 250, 250)
BLOCKCOLORFILLBLUE = (68, 85, 90)
BLOCKCOLOR = (220,220,220)
# BOARDCOLOR = (210,180,140)
BOARDCOLOR = (0,0,0)
BLACK = (0, 0, 0)

class Game: 
    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Taiji")

    def display(self):
        pygame.display.flip()
        pygame.display.update()

    def draw_grid(self):
        self.block_size = 50
        for x in range(225, BOARDWINDOWWIDTH, self.block_size):
            for y in range(225, BOARDWINDOWHEIGHT, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

        # TODO: make a for-loop of this
        # Draw rect option 1 - Player 1
        rect = pygame.Rect(20, 225, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(20, 225+50, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

        # Draw rect option 2 - Player 1
        rect = pygame.Rect(20, 275+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(20+50, 275+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

        # Draw rect option 3 - Player 1
        rect = pygame.Rect(20, 350+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(20, 425+50, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

        # Draw rect option 4 - Player 1
        rect = pygame.Rect(20, 475+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(20+50, 475+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

        # Draw rect option 1 - Player 2
        rect = pygame.Rect(830, 225, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(830, 225+50, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        
        # Draw rect option 2 - Player 2
        rect = pygame.Rect(830, 275+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(830-50, 275+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        
        # Draw rect option 3 - Player 3
        rect = pygame.Rect(830, 350+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(830, 425+50, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        
        # Draw rect option 4 - Player 4
        rect = pygame.Rect(830, 475+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)
        rect = pygame.Rect(830-50, 475+75, self.block_size, self.block_size)
        pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

    def add_block(self):
        # TODO: support user functionality to add block
        pass

if __name__ == "__main__":
    game = Game()
    game_active = True
    while game_active:
        game.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
        game.game_window.fill((BOARDCOLOR))        
        game.draw_grid()
        pygame.display.flip()

pygame.quit()
quit()