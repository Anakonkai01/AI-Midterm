class Node: # TODO: need to do something with this class because it not done 
    def __init__(self, state, action = None, parent = None, pathCost =None, H_1=None):
        self.state = state 
        self.action = action 
        self.parent = parent 
        self.pathCost = pathCost 
        self.H_1 = H_1
        self.ID = str(state)

    def __str__(self):
        return  '\n'.join(''.join(str(num) if num != 0 else '_' for num in row) for row in self.get_state().get_board())

    def __lt__(self, other):
        return self.pathCost + self.H_1 < other.pathCost + other.H_1

    def get_state(self):
        return self.state
    
    def get_action(self):
        return self.action
    
    def get_path_cost(self):
        return self.pathCost

    def get_parent(self):
        return self.parent

    def get_id(self):
        return self.ID

    #For visualize the result  
    def get_str_node(self):
        return str(self)
    
    def getCost(self):
        return 1
    
    def set_H(self, H):
        self.H_1 = H
    
    def set_G(self, G):
        self.pathCost = G

    #Get all successors of a node
    def getSuccessors(self): 
        successors = []
        state_of_node = self.get_state()
        for action in state_of_node.getActions():
            new_state = state_of_node.getSuccessor(action)
            cost = new_state.getCost(state_of_node, action)
            successors.append(Node(new_state, action, self, cost))
        return successors


    #Draw a node and its edge which is associated with its parent
    def draw(self, dot):
        dot.node(self.get_id(), self.get_str_node(),shape = "square")
        if self.get_parent() is not None:
            dot.edge(self.get_parent().get_id(), self.get_id(), self.get_action())
