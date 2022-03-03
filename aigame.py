import pygame
from pygame.locals import * 

from OpenGL.GL import *
from OpenGL.GLU import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

class Game: 
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.game_window.fill((0, 0, 0))
        pygame.display.set_caption("AI Game")
        self.clock.tick()
        # pygame.display.flip()

    def display(self):
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game_active = True
    # game.display()
    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
        
        game.game_window.fill((0, 0, 0))
        pygame.display.flip()
        pygame.display.update()
        # game.display()