from agent_thordur import AgentAPI
from board_thordur import BoardAPI

# Test code that makes the agent make 30 random moves
# Can be changed to alternate between waiting for player 
# move, and getting move from the agent.
board = BoardAPI()
player1 = AgentAPI(name='Player 1', board=board)
player2 = AgentAPI(name='Player 2', board=board)

for i in range(15):
	player1.make_move()
	player2.make_move()