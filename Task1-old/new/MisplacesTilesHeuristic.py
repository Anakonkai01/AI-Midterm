import Heuristic



class MisplacesTilesHeuristic(Heuristic.HeuristicFunction):
    def __init__(self):
        pass

    def getHeuristic(self, state, goalStates):
        goal = goalStates # check this because this is a list of goal states so we need to check this
        
        min_misplaced = 9
        
        for goalState in goal:
            misplaced = 0
            for i in range(3):
                for j in range(3):
                    if state.board[i][j] != goalState.board[i][j]:
                        misplaced += 1

            if misplaced < min_misplaced:
                min_misplaced = misplaced
        
        return min_misplaced