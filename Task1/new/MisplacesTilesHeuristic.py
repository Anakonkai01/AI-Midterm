import Heuristic



class MisplacesTilesHeuristic(Heuristic):
    def __init__(self):
        pass

    def getHeuristic(self, state, goalStates):
        goal = goalStates # check this because this is a list of goal states so we need to check this

        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal[i][j]:
                    misplaced += 1
        return misplaced