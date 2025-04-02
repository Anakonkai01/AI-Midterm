import Heuristic


class ManhattanHeuristic(Heuristic.HeuristicFunction):
    def __init__(self):
        pass

    # Ví dụ trong file ManhattanHeuristic.py
    def getHeuristic(self, state, goalStates):
        list_distance = []
        
        for goal in goalStates:
            # Giả sử goal là đối tượng EightPuzzleState, lấy board của goal
            board_goal = goal.get_board()  # hoặc goal.board nếu board là thuộc tính công khai
            goal_pos = {}
            for i in range(3):
                for j in range(3):
                    goal_pos[board_goal[i][j]] = (i, j)
            
            distance = 0
            # Giả sử state là đối tượng EightPuzzleState
            board_state = state.get_board()
            for i in range(3):
                for j in range(3):
                    tile = board_state[i][j]
                    if tile != 0:
                        gx, gy = goal_pos[tile]
                        distance += abs(gx - i) + abs(gy - j)
            list_distance.append(distance)
        
        return min(list_distance)

