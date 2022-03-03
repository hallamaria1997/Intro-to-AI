import pygame
from pygame.locals import * 
from block import Block
from grid import Grid

# GAME WINDOW
WINDOWWIDTH = 900
WINDOWHEIGHT = 900

# COLORS
BLOCKCOLORFILLWHITE = (250, 250, 250)
BLOCKCOLORFILLBLUE = (4, 217, 255)
BOARDCOLOR = (0,0,0)

class Game: 
    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Taiji")
        self.grid = Grid()

    def display(self):
        pygame.display.flip()
        pygame.display.update()

    def draw_grid(self):
        self.block_size = 50
        self.grid.display(self.game_window)

        # TODO: temporary solution - do a for-loop
        # BLOCKS  
        # B1
        b1 = Block()
        b1.draw(20, 225, self.game_window, BLOCKCOLORFILLWHITE)
        
        b2 = Block()
        b2.draw(20, 225+50, self.game_window, BLOCKCOLORFILLBLUE)

        # B2
        b3 = Block()
        b3.draw(20, 275+75, self.game_window, BLOCKCOLORFILLWHITE)

        b33 = Block()
        b33.draw(20+50, 275+75, self.game_window, BLOCKCOLORFILLBLUE)

        # B3
        b4 = Block()
        b4.draw(20, 350+75, self.game_window, BLOCKCOLORFILLBLUE)

        b5 = Block()
        b5.draw(20, 350+75+50, self.game_window, BLOCKCOLORFILLWHITE)

        # B4
        b6 = Block()
        b6.draw(20, 475+75, self.game_window, BLOCKCOLORFILLBLUE)

        b7 = Block()
        b7.draw(20+50, 475+75, self.game_window, BLOCKCOLORFILLWHITE)

        # B5
        b8 = Block()
        b8.draw(830, 225, self.game_window, BLOCKCOLORFILLBLUE)

        b8 = Block()
        b8.draw(830, 225+50, self.game_window, BLOCKCOLORFILLWHITE)

        # B6
        b8 = Block()
        b8.draw(830, 275+75, self.game_window, BLOCKCOLORFILLBLUE)

        b9 = Block()
        b9.draw(830-50, 275+75, self.game_window, BLOCKCOLORFILLWHITE)

        # B7 
        b10 = Block()
        b10.draw(830, 350+75, self.game_window, BLOCKCOLORFILLBLUE)

        b11 = Block()
        b11.draw(830, 425+50, self.game_window, BLOCKCOLORFILLWHITE)

        # B8
        b12 = Block()
        b12.draw(830, 475+75, self.game_window, BLOCKCOLORFILLBLUE)

        b13 = Block()
        b13.draw(830-50, 475+75, self.game_window, BLOCKCOLORFILLWHITE)

        self.blocks = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13]

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