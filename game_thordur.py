from agent_thordur import AgentAPI

# Test code that makes the agent make 30 random moves
# Can be changed to alternate between waiting for player 
# move, and getting move from the agent.
agentAPI = AgentAPI()

for i in range(30):
	agentAPI.make_move()