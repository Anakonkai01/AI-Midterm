

class Node: # TODO: need to do something with this class because it not done 
    def __init__(self, state, action, parent, pathCost, H_1):
        self.state = state
        self.action = action
        self.parent = parent
        self.pathCost = pathCost
        self.H_1 = H_1
        self.ID = str(state)

    def __lt__(self, other):
        return self.pathCost + self.H_1 < other.pathCost + other.H_1
    
    