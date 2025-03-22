import random as r
class Problem:
    def __init__(self):
        self.initial_state = [[r.randint(0,8) for _ in range(3)] for _ in range((3))]  
        self.goal_states =  [
                                [[j if j != 9 else 0 for j in range(row, row + 3)] for row in range(1, 9, 3)] , # 1->8, góc phải bên dưới
                                [[j for j in range(row, row - 3, -1)] for row in range(8, -1, -3)], # 8->1, góc phải bên dưới 
                                [[j for j in range(row, row + 3)] for row in range(0, 9, 3)], # 1->8, góc trái bên trên
                                [[j if j != 9 else 0 for j in range(row, row - 3, -1)] for row in range(9, 0, -3)], # 8->1, góc trái bên trên
                           ]
    def get_goal_states(self):
        return self.goal_states
        
