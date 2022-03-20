from turtle import width
import pygame
from pygame.locals import * 
from block import Block
from grid import Grid
from agent import AgentAPI
import numpy as np
import sys

# GAME WINDOW
WINDOWWIDTH = 900
WINDOWHEIGHT = 900

# COLORS
BLOCKCOLORFILLWHITE = (220, 220, 220)
BLOCKCOLORFILLBLUE = (0, 145, 255)
BOARDCOLOR = (0,0,0)
BLOCKCOLOR = (245,0,124)

BLOCKCOLORFILLEXTRAWHITE= (255,255,255)
BLOCKCOLORFILLEXTRABLUE = (172,217,252)

class Game: 
    selectedTile = ""
    tileSelected = False
    validated = False
    agentsTurn = False
    game_active = True
    game_over = False
    width = 0
    height = 0
    screen = None
    player = 1
    agentNum = None
    firstMove = True

    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Taiji")
        self.agentNum  = int(sys.argv[1])
        res = (900,900)
        self.screen = pygame.display.set_mode(res)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.grid = Grid()
        self.board = [0]*9*9
        self.agent = AgentAPI(name='Computer', board=self)
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

    def draw_over(self):
        rect = pygame.Rect(140, 140, 620, 620)
        pygame.draw.rect(self.game_window, (0,0,0), rect, 500)

        font = pygame.font.Font(pygame.font.get_default_font(), 56)
        font2 = pygame.font.Font(pygame.font.get_default_font(), 30)
        color = (255,255,255)
        
        blackscore, whitescore = self.get_scores()
        winner = ""

        if(blackscore > whitescore):
            winner = "Blue wins with " + str(blackscore) + " points!!!"
        else:
            winner = "White wins with " + str(whitescore) + " points!!!"
        
        # rendering a text written in
        # this font

        gameOverText = font.render('~ Game Over ~' , True , color)
        wonText = font2.render(winner , True , color)

        self.screen.blit(gameOverText , (self.width/2 - 200 ,self.height/2 - 90)) 
        self.screen.blit(wonText , (self.width/2 - 190 ,self.height/2 + 10)) 

    def draw_blocks(self):

        for d in self.white_block_info:
            b = Block(d['type'])
            b.draw(d['x'], d['y'], self.game_window, BLOCKCOLORFILLWHITE)
            self.blocks.append(b)

        for d in self.blue_block_info:
            b = Block(d['type'])
            b.draw(d['x'], d['y'], self.game_window, BLOCKCOLORFILLBLUE)
            self.blocks.append(b)

    def getAgentMove(self, player):
        while(self.agentsTurn == True):
            pos, self.selectedType = self.agent.make_move(player)
            mod_pos = ((50*pos[1])+225, (50*pos[0])+225)
            self.placeTile(mod_pos)

    def selectTile(self, pos):
        for b in self.blocks:
            if b.get_rect().collidepoint(pos):
                self.tileSelected = True
                if b.block_type == 1:
                    self.selectedType = 1
                    self.selectedTile = "1"
                elif b.block_type == 2:
                    self.selectedType = 2
                    self.selectedTile = "2"
                elif b.block_type == 3:
                    self.selectedType = 3
                    self.selectedTile = "3"
                elif b.block_type == 4:
                    self.selectedType = 4
                    self.selectedTile = "4"
    
    def validateMove(self, index):
        if(self.selectedType == 1 \
            and (index + 1) <= 72 \
            and self.board[index] == 0 \
            and self.board[index + 9] == 0):
            return True

        elif(self.selectedType == 2 \
            and (index + 1) % 9 > 0 \
            and self.board[index] == 0 \
            and self.board[index + 1] == 0):
            return True

        elif(self.selectedType == 3 \
            and (index + 1) <= 72 \
            and self.board[index] == 0 \
            and self.board[index + 9] == 0):
            return True

        elif(self.selectedType == 4 \
            and (index + 1) % 9 > 0 \
            and self.board[index] == 0 \
            and self.board[index + 1] == 0):
            return True
    
    def get_board(self):
        return np.reshape(self.board, (9,9))

    def placeTile(self, pos):
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
                    self.board[index] = 2
                    self.board[index + 9] = 1
                    self.grid.rectsColors[index] = BLOCKCOLORFILLBLUE
                    self.grid.rectsColors[index + 9] = BLOCKCOLORFILLWHITE
                    self.grid.width[index] = 100
                    self.grid.width[index + 9] = 100
                    self.tileSelected=[]
                    self.validated = False
                    self.agentsTurn = not self.agentsTurn
                    return
                elif(self.selectedType == 4  and self.validated):
                    self.board[index] = 2
                    self.board[index + 1] = 1
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
        if (self.width/2 + 10 <= pos[0] <= self.width/2+150 and self.height - 50 <= pos[1] <= self.height - 10):
            pygame.quit()

        if (self.width/2 -150 <= pos[0] <= self.width/2 - 10 and self.height - 50 <= pos[1] <= self.height - 10):
            game.reset()

        if(self.agentNum == 2 and not self.game_over):

            if (self.agentNum == 2 and 30 <= pos[0] <= 30 + 180 and 30 <= pos[1] <= 30 + 40):
                if(self.firstMove):
                    pos, self.selectedType = self.agent.random_move()
                    mod_pos = ((50*pos[1])+225, (50*pos[0])+225)
                    self.placeTile(mod_pos)
                    self.firstMove = False

                self.agentsTurn = True
                self.getAgentMove(self.player)

            if(self.player == 1):
                self.player = 2
            else:
                self.player = 1
        else:

            if(self.agentsTurn == False): 
                if(self.tileSelected):
                    self.placeTile(pos) 
                self.selectTile(pos)

            if(self.agentsTurn):
                self.getAgentMove(self.player)

        return

    def checkIfGameOver(self):
        if(len(self.find_paths(self.get_board(), 0)[0]) < 2):
            self.game_over = True

    def get_available_moves(self,board):
        moves = []
        rows, cols = board.shape
        dirs = ['l', 'r', 'u', 'd']

        for i in range(rows):
            for j in range(cols):
                for d in dirs:
                    pos = (i,j)
                    r,c = self.get_r_c(d)
                    if self.position_ok(board,pos, r, c):
                        moves.append((pos, r,c,))
        return moves
    
    def get_r_c(self, dir):
        # Translate the direction into numbers
        if dir == 'r':
            r = 0
            c = 1
        elif dir == 'l':
            r = 0
            c = -1
        elif dir == 'u':
            r = -1
            c = 0
        elif dir == 'd':
            r = 1
            c = 0
        return r, c

    def position_ok(self, board, pos, r, c):
        n_rows, n_cols = board.shape
        if pos[0] + r + 1 >= n_rows:
            return False
        if pos[0] + r < 0:
            return False
        if pos[1] + c + 1 >= n_cols:
            return False
        if pos[1] + c < 0:
            return False
        if (board[pos] != 0 or board[(pos[0]+r, pos[1]+c)] != 0):
            return False
        return True

    def is_adj(self, c1, c2):
        s = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
        return s == 1

    def merge_paths(self, adj_lists):
		# Merge the neighbour lists into complete paths
        merges = 1
        while merges != 0:
            merges = 0
            for i, a in enumerate(adj_lists):
                for j, b in enumerate(adj_lists):
                    if j != i and len(set(adj_lists[i]).intersection(set(b))) > 0:
                        merges += 1
                        new_set = list(set(adj_lists[i]).union(b))
                        adj_lists[i] = new_set
                        adj_lists[j] = []

		# Sort by length and delete empty paths
        adj_lists = sorted(adj_lists, key=lambda l: len(l), reverse=True)
        adj_lists = [i for i in adj_lists if len(i) > 0]
        return adj_lists

    def find_paths(self, board, n):
		# Locations of the value n on the board
        locs = np.where(board==n)
        coords = list(zip(locs[0], locs[1]))
        adj_lists = []

		# Finds the neighbour of each n-value
        for i, c1 in enumerate(coords):
            adj_lists.append([c1])
            for j, c2 in enumerate(coords):
                if i != j and self.is_adj(c1, c2):
                    adj_lists[i].append(c2)
		
		# Merges the neighbors into paths
        paths = self.merge_paths(adj_lists)

        return paths

    def draw_buttons(self):

        # white color
        color = (255,255,255)

        # light shade of the button
        color_light = (170,170,170)
        
        # dark shade of the button
        color_dark = (100,100,100)

        #print(pygame.font.get_fonts())

        # defining a font
        smallfont = pygame.font.Font(pygame.font.get_default_font(), 35)
        smallerfont = pygame.font.Font(pygame.font.get_default_font(), 25)
        
        # rendering a text written in
        # this font
        quitText = smallfont.render('quit' , True , color)
        restartText = smallfont.render('restart' , True , color)
        nextMoveText = smallerfont.render('get next move' , True , color)

        pos = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade 
        if (self.width/2 + 10 <= pos[0] <= self.width/2+150 and self.height - 50 <= pos[1] <= self.height-10):
            pygame.draw.rect(self.screen,color_light,[self.width/2,self.height - 50,140,40])
            
        else:
            pygame.draw.rect(self.screen,color_dark,[self.width/2 + 10,self.height - 50,140,40])


        if (self.width/2 - 150 <= pos[0] <= self.width/2 - 10 and self.height - 50 <= pos[1] <= self.height-10):
            pygame.draw.rect(self.screen,color_light,[self.width/2 - 150,self.height - 50,140,40])
            
        else:
            pygame.draw.rect(self.screen,color_dark,[self.width/2 - 150,self.height - 50,140,40])

        if(not self.game_over):
            if (self.agentNum == 2 and 30 <= pos[0] <= 30 + 180 and 30 <= pos[1] <= 30 + 40):
                pygame.draw.rect(self.screen,color_light,[30,30,180,40])
                
            elif self.agentNum == 2:
                pygame.draw.rect(self.screen,color_dark,[30, 30 ,180,40])

            if(self.agentNum == 2):
                self.screen.blit(nextMoveText , (30, 30)) 

        # superimposing the text onto our button
        self.screen.blit(quitText , (self.width/2+25 + 10,self.height - 50)) 
        self.screen.blit(restartText , (self.width/2+25 - 160,self.height - 50)) 

    def draw_name(self):
        color = (255,255,255)
        taijiFont = pygame.font.Font(pygame.font.get_default_font(), 60)
        taijiText = taijiFont.render('TAIJI' , True , color)
        self.screen.blit(taijiText , (self.width/2 - 70 , 20)) 


    def reset(self):
        self.grid.reset()
        self.board = [0]*9*9
        self.firstMove = True
        self.game_over = False

    def get_scores(self):
        white_paths = self.find_paths(self.get_board(), 1)
        black_paths = self.find_paths(self.get_board(), 2)

        blackscore = 0
        whitescore = 0

        if(len(white_paths) == 1 and len(black_paths) == 1):
            blackscore = len(black_paths[0])
            whitescore = len(white_paths[0])

        elif(len(white_paths) == 1 and len(black_paths) == 2):
            blackscore = len(black_paths[0]) + len(black_paths[1])
            whitescore = len(white_paths[0])

        elif(len(white_paths) == 2 and len(black_paths) == 1):
            blackscore = len(black_paths[0])
            whitescore = len(white_paths[0]) + len(white_paths[1])
        elif (len(white_paths) >= 2 and len(black_paths) >= 2):
            blackscore = len(black_paths[0]) + len(black_paths[1])
            whitescore = len(white_paths[0]) + len(white_paths[1])

        return blackscore, whitescore


    def draw_scores(self):

        blackscore, whitescore = self.get_scores()
        black = "Blue: " + str(blackscore)
        white = "White: " + str(whitescore)

        color = (255,255,255)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        blackText = font.render(black , True , color)
        whiteText = font.render(white , True , color)
        self.screen.blit(blackText , (30 , self.height - 100)) 
        self.screen.blit(whiteText , (self.width - 100 , self.height - 100)) 

    def draw_player(self):
        if(self.agentNum == 1):

            black = "You"

            color = (255,255,255)
            font = pygame.font.Font(pygame.font.get_default_font(), 30)
            blackText = font.render(black , True , color)
            self.screen.blit(blackText , (30 , self.height - 140)) 

    def draw_selectedType(self):
        if(self.tileSelected):
            if(self.selectedTile == "1"):
                info1 = self.white_block_info[0]
                info2 = self.blue_block_info[0]
            elif(self.selectedTile == "2"):
                info1 = self.white_block_info[1]
                info2 = self.blue_block_info[1]
            elif(self.selectedTile == "3"):
                info1 = self.white_block_info[2]
                info2 = self.blue_block_info[2]
            elif(self.selectedTile == "4"):
                info1 = self.white_block_info[3]
                info2 = self.blue_block_info[3]


            b = Block(info1['type'])
            b.draw(info1['x'], info1['y'], self.game_window, BLOCKCOLORFILLEXTRAWHITE)

            b = Block(info2['type'])
            b.draw(info2['x'], info2['y'], self.game_window, BLOCKCOLORFILLEXTRABLUE)



if __name__ == "__main__":

    game = Game()
    index = 0
    while game.game_active:
        game.draw_grid()
        game.draw_blocks()   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                game.action(pos)
                index += 1

        game.game_window.fill((BOARDCOLOR)) 
        game.draw_grid() 
        game.draw_blocks() 
        game.draw_buttons()  
        game.draw_name()
        game.draw_scores()
        game.draw_player()
        game.draw_selectedType()

        game.checkIfGameOver()

        if(game.game_over):
            game.draw_over()

        pygame.display.flip()


pygame.quit()
quit()