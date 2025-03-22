import Heuristic


class ManhattanHeuristic(Heuristic):
    def __init__(self):
        pass

    def getHeuristic(self, state, goalStates):
        goal = goalStates # this also needs to be checked because this is a list of goal states

        goal_pos = {goal[i][j]: (i, j) for i in range(3) for j in range(3)}

        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i, goal_j = goal_pos[state[i][j]]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance