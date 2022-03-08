import pygame

class Block:
    rect = []

    def __init__(self, block_type):
        self.block_size = 50
        self.block_type = block_type

    def draw(self, x, y, game_window, color):
        rect = pygame.Rect(x, y, self.block_size, self.block_size)
        self.rect = rect
        pygame.draw.rect(game_window, color, rect, 0)

    def get_rect(self):
        return self.rect