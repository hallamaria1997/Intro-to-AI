import pygame
from pygame.locals import * 

WINDOWWIDTH = 675
WINDOWHEIGHT = 675
BLOCKCOLOR = (250, 250, 250)
BOARDCOLOR = (210,180,140)
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
        self.block_size = 75
        for x in range(0, WINDOWWIDTH, self.block_size):
            for y in range(0, WINDOWHEIGHT, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.game_window, BLOCKCOLOR, rect, 1)

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