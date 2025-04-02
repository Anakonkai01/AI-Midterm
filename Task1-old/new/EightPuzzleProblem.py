import Problem
import Node

class EightPuzzleProblem(Problem.Problem):
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state # use state
        self.goal_state = goal_state # use tuple of state

    def getInitialState(self):
        return self.initial_state

    def isGoalState(self, state):
        return state in self.goal_state
    
    def getSuccessors(self, state): # ráng chỉnh lại là trả về  1 list các node chứ ko phải các thành phần riêng lẻ
        successors = []
        node_of_state = Node.Node(state)
        for action in state.getActions():
            new_state = state.getSuccessor(action)
            cost = self.getCost(state, action)
            successors.append(Node.Node(new_state, action, node_of_state, cost))
        return successors
        
    def getCost(self, state, action):
        return 1

# Hoàn thành phần getSuccessors trả về các node