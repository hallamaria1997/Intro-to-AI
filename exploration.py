import pygame
from pygame.locals import * 
from block import Block
from grid import Grid
from agent import Agent


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

    def display(self):
        pygame.display.flip()
        pygame.display.update()

    def draw_grid(self):
        self.block_size = 50
        self.grid.display(self.game_window)

    def draw_blocks(self):

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

        b88 = Block()
        b88.draw(830, 225+50, self.game_window, BLOCKCOLORFILLWHITE)

        # B6
        b9 = Block()
        b9.draw(830, 275+75, self.game_window, BLOCKCOLORFILLBLUE)

        b99 = Block()
        b99.draw(830-50, 275+75, self.game_window, BLOCKCOLORFILLWHITE)

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

        self.blocks = [b1, b2, b3, b33, b4, b5, b6, b7, b8, b88, b9, b99, b10, b11, b12, b13]

    def getAgentMove(self):
        while(self.agentsTurn == True):
            pos = self.agent.getRandomMove(self.selectedType)
            self.placeTile(pos)

    def selectTile(self, pos):
        for b in self.blocks:
            if b.get_rect().collidepoint(pos):
                self.selectedTile = b.get_rect()
                self.tileSelected = True

                if (b == self.blocks[0] or b == self.blocks[1] or b == self.blocks[8] or b == self.blocks[9]):
                    self.selectedType = 1
                elif (b == self.blocks[2] or b == self.blocks[3] or b == self.blocks[10] or b == self.blocks[11]):
                    self.selectedType = 2
                elif (b == self.blocks[4] or b == self.blocks[5] or b == self.blocks[12] or b == self.blocks[13]):
                    self.selectedType = 3
                elif (b == self.blocks[6] or b == self.blocks[7] or b == self.blocks[14] or b == self.blocks[15]):
                    self.selectedType = 4
    
    def validateMove(self, index):
        if(self.selectedType == 1 \
            and (index + 1) % 9 > 0 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 1] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 2 \
            and (index + 1) < 72 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 9] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 3 \
            and (index + 1) % 9 > 0 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 1] == BLOCKCOLOR):
            return True

        elif(self.selectedType == 4 \
            and (index + 1) < 72 \
            and self.grid.rectsColors[index] == BLOCKCOLOR \
            and self.grid.rectsColors[index + 9] == BLOCKCOLOR):
            return True

    def placeTile(self,pos):
        index = 0
        for r in self.grid.rects:
            if r.collidepoint(pos):
                self.validated = self.validateMove(index)
                if(self.selectedType == 1 and self.validated):
                    self.grid.rectsColors[index] = BLOCKCOLORFILLWHITE
                    self.grid.rectsColors[index + 1] = BLOCKCOLORFILLBLUE
                    self.grid.width[index] = 100
                    self.grid.width[index + 1] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 2  and self.validated):
                    self.grid.rectsColors[index] = BLOCKCOLORFILLWHITE
                    self.grid.rectsColors[index + 9] = BLOCKCOLORFILLBLUE
                    self.grid.width[index] = 100
                    self.grid.width[index + 9] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 3  and self.validated):
                    self.grid.rectsColors[index] = BLOCKCOLORFILLBLUE
                    self.grid.rectsColors[index + 1] = BLOCKCOLORFILLWHITE
                    self.grid.width[index] = 100
                    self.grid.width[index + 1] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 4  and self.validated):
                    self.grid.rectsColors[index] = BLOCKCOLORFILLBLUE
                    self.grid.rectsColors[index + 9] = BLOCKCOLORFILLWHITE
                    self.grid.width[index] = 100
                    self.grid.width[index + 9] = 100
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