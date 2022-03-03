import pygame

class Block:
    def __init__(self):
        self.block_size = 50

    def draw(self, x, y, game_window, color):
        rect = pygame.Rect(x, y, self.block_size, self.block_size)
        pygame.draw.rect(game_window, color, rect, 0)