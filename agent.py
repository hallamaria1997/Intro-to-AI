import random

class Agent:

   #def __init__(self):
    

    def getRandomMove(self, selectedType):
        print("agent tries placing random move")
        self.selectedType = random.randint(1,4)
        print(self.selectedType)
        x = random.randint(280,625)
        y = random.randint(280,625)
        pos = (x,y)
        print(pos)
        return pos