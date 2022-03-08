import pygame
from pygame.locals import * 
from block import Block
from grid import Grid
from agent import Agent
import numpy as np

# GAME WINDOW
WINDOWWIDTH = 900
WINDOWHEIGHT = 900

# COLORS
BLOCKCOLORFILLWHITE = (250, 250, 250)
BLOCKCOLORFILLBLUE = (4, 217, 255)
BOARDCOLOR = (0,0,0)
BLOCKCOLOR = (245,0,124)

class Game: 
    selectedTile = []
    tileSelected = False
    validated = False
    agentsTurn = False

    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Taiji")
        self.grid = Grid()
        self.agent = Agent()
        self.board = [0]*9*9
        self.white_block_info = [{'x': 20, 'y': 225, 'type': 1}, 
                                {'x': 20,'y': 350, 'type': 2}, 
                                {'x': 20, 'y': 475, 'type': 3},
                                {'x': 70, 'y': 550, 'type': 4}, 
                                {'x': 830, 'y': 225, 'type': 1},
                                {'x': 780, 'y': 350, 'type': 2},
                                {'x': 830, 'y': 475, 'type': 3},
                                {'x': 780, 'y': 550, 'type': 4},
                                {'x': 830, 'y': 550, 'type': 4}]
        self.blue_block_info = [{'x': 20, 'y': 275, 'type': 1}, 
                                {'x': 70,'y': 350, 'type': 2}, 
                                {'x': 20, 'y': 425, 'type': 3},
                                {'x': 20, 'y': 550, 'type': 4}, 
                                {'x': 830, 'y': 275, 'type': 1},
                                {'x': 830, 'y': 350, 'type': 2},
                                {'x': 830, 'y': 425, 'type': 3}, 
                                {'x': 780, 'y': 550, 'type': 4}]
        self.blocks = []
    
    def display(self):
        pygame.display.flip()
        pygame.display.update()

    def draw_grid(self):
        self.block_size = 50
        self.grid.display(self.game_window)

    def draw_blocks(self):

        for d in self.white_block_info:
            b = Block(d['type'])
            b.draw(d['x'], d['y'], self.game_window, BLOCKCOLORFILLWHITE)
            self.blocks.append(b)

        for d in self.blue_block_info:
            b = Block(d['type'])
            b.draw(d['x'], d['y'], self.game_window, BLOCKCOLORFILLBLUE)
            self.blocks.append(b)

    def getAgentMove(self):
        while(self.agentsTurn == True):
            pos, self.selectedType = self.agent.getRandomMove(self.selectedType)
            self.placeTile(pos)

    def selectTile(self, pos):
        for b in self.blocks:
            if b.get_rect().collidepoint(pos):
                self.selectedTile = b.get_rect()
                self.tileSelected = True
                if b.block_type == 1:
                    self.selectedType = 1
                elif b.block_type == 2:
                    self.selectedType = 2
                elif b.block_type == 3:
                    self.selectedType = 3
                elif b.block_type == 4:
                    self.selectedType = 4
    
    def validateMove(self, index):
        if(self.selectedType == 1 \
            and (index + 1) < 72 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 9] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 2 \
            and (index + 1) % 9 > 0 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 1] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 3 \
            and (index + 1) < 72 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 9] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 4 \
            and (index + 1) % 9 > 0 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 1] == BLOCKCOLOR):
            return True
    
    def get_board(self):
        return np.reshape(self.board, (9,9))

    def placeTile(self, pos):
        print(np.reshape(self.board, (9,9)))
        index = 0
        for r in self.grid.rects:
            if r.collidepoint(pos):
                self.validated = self.validateMove(index)
                if(self.selectedType == 1 and self.validated):
                    self.board[index] = 1
                    self.board[index + 9] = 2 
                    self.grid.rectsColors[index] = BLOCKCOLORFILLWHITE
                    self.grid.rectsColors[index + 9] = BLOCKCOLORFILLBLUE
                    self.grid.width[index] = 100
                    self.grid.width[index + 9] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 2  and self.validated):
                    self.board[index] = 1
                    self.board[index + 1] = 2 
                    self.grid.rectsColors[index] = BLOCKCOLORFILLWHITE
                    self.grid.rectsColors[index + 1] = BLOCKCOLORFILLBLUE
                    self.grid.width[index] = 100
                    self.grid.width[index + 1] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 3  and self.validated):
                    self.board[index] = 1
                    self.board[index + 9] = 2 
                    self.grid.rectsColors[index] = BLOCKCOLORFILLBLUE
                    self.grid.rectsColors[index + 9] = BLOCKCOLORFILLWHITE
                    self.grid.width[index] = 100
                    self.grid.width[index + 9] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 4  and self.validated):
                    self.board[index] = 1
                    self.board[index + 1] = 2 
                    self.grid.rectsColors[index] = BLOCKCOLORFILLBLUE
                    self.grid.rectsColors[index + 1] = BLOCKCOLORFILLWHITE
                    self.grid.width[index] = 100
                    self.grid.width[index + 1] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
            index += 1
        return

    def action(self, pos):   
        if(self.agentsTurn == False): 
            if(self.tileSelected):
                self.placeTile(pos) 
            self.selectTile(pos)

        if(self.agentsTurn):
            self.getAgentMove()
        return

    def checkIfGameOver(self):
        for i in range(0,8,1):
            for j in range(0,8,1):
                self.grid.width[i*j + j] = 100

if __name__ == "__main__":
    game = Game()
    game_active = True
    while game_active:
        game.draw_grid()
        game.draw_blocks()   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                game.action(pos)
        game.game_window.fill((BOARDCOLOR)) 
        game.draw_grid() 
        game.draw_blocks()      
        pygame.display.flip()

pygame.quit()
quit()