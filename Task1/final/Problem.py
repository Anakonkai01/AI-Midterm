import Node
class Problem:
    #Save the intial state and goal states of problem 
    def __init__(self, initial_state, goal_states):
        self.initial_state = initial_state 
        self.goal_states = goal_states 
 
    def getInitialState(self):
        return self.initial_state

    def isGoalState(self, state):
        return state in self.goal_states

    def getSuccessors(self, state):
        node = Node.Node(state)
        return node.getSuccessors()
 
    def getCost(self, state, action):
        node = Node.Node(state)
        return node.getCost()
     
    def get_goal_states(self):
        return self.goal_states 
    
    def get_initial_state(self):
        return self.initial_state