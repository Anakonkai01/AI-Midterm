class Heuristic:
    def __init__(self, type):
        self.heuristic_type = type
        self.Heuristics =    {
                                "EnhancedManhattan": self.EnhancedManhattan,
                                "EnhancedMissplace": self.EnhancedMissplace
                            }
        self.heuristic_func = self.Heuristics[self.heuristic_type]
        
    def Num_linear_conflict(self,current_board, goal_board):
        number_of_conflicts = 0
        look_up_conflict = lambda a,b,c: [[b,a,c], [c,b,a], [a,c,b]] #Bảng tra cứu các hoán vị gây xung đột để dễ dàng kiểm tra
        # Xung đột: các ô các bị đảo ngược vị trí trên cùng 1 hàng/ cột (hay còn gọi là cản trở nhau) 
        for row in range(len(current_board)): #Kiểm tra xung đột trên các hàng
            current_row = current_board[row]
            goal_row = goal_board[row] 
            a,b,c = goal_row[0], goal_row[1], goal_row[2] 
            potential_conflict_rows = look_up_conflict(a,b,c)
            if current_row in potential_conflict_rows:
                if current_row == potential_conflict_rows[1]:
                    number_of_conflicts += 2 
                    continue
                number_of_conflicts += 1
        for col in range(len(current_board)): #Kiểm tra xung đột trên các cột
            current_row = [current_board[row][col] for row in range(len(current_board))]
            goal_row= [goal_board[row][col] for row in range(len(goal_board))]
            a,b,c = goal_row[0], goal_row[1], goal_row[2] 
            potential_conflict_rows = look_up_conflict(a,b,c)
            if current_row in potential_conflict_rows:
                if current_row == potential_conflict_rows[1]:
                    number_of_conflicts += 2 
                    continue
                number_of_conflicts += 1 
        return number_of_conflicts    
        
    #Tổng số khoảng cách Manhattan với số xung đột theo hàng & cột
    def EnhancedManhattan(self, state, goalStates):
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
            list_distance.append(distance + self.Num_linear_conflict(board_state, board_goal))
        return min(list_distance) 
    
    #Tổng sai số vị trí với xung đột hàng & cột
    def EnhancedMissplace(self, state, goalStates):
        goal = goalStates # check this because this is a list of goal states so we need to check this 
        min_misplaced = 9
        for goalState in goal:
            misplaced = 0
            for i in range(3):
                for j in range(3):
                    if state.board[i][j] != goalState.board[i][j]:
                        misplaced += 1

            min_misplaced += self.Num_linear_conflict(state.get_board(), goalState.get_board())

            if misplaced < min_misplaced:
                min_misplaced = misplaced
        return min_misplaced 
    
    def getHeuristic(self, state, goalStates):
        return self.heuristic_func(state, goalStates)
    
 