import Problem

class EightPuzzleProblem(Problem):
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state # use state
        self.goal_state = goal_state # use list<state>

    def getInitialState(self):
        return self.initial_state

    def isGoalState(self, state):
        return state.get_board() in self.goal_state
    
    def getSuccessors(self, state):
        successors = []
        for action in state.getActions():
            new_state = state.getSuccessor(action)
            cost = self.getCost(state, action)
            successors.append((new_state, action, cost))
        return successors
        
    def getCost(self, state, action):
        return 1
