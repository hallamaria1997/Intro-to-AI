import pygame

class Block:
    rect = []

    def __init__(self):
        self.block_size = 50

    def draw(self, x, y, game_window, color):
        rect = pygame.Rect(x, y, self.block_size, self.block_size)
        self.rect = rect
        pygame.draw.rect(game_window, color, rect, 0)

    def get_rect(self):
        return self.rect