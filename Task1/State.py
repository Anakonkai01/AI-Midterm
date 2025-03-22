from Tools import Tools
from Problem import Problem
class State:
    Problem_Instance = Problem()
    def __init__(self, matrix):
        self.matrix = matrix
        self.hash_matrix = self.hash_func(self.matrix)

    
    def hash_func(self):
        return hash(tuple(tuple(row) for row in self.matrix))
    
    def __hash__(self):
        return self.hash_matrix

    def __eq__(self, other):
        return isinstance(other, State) and self.hash_matrix == other.hash_matrix

    def get_matrix(self):
        return self.data

    #Kiểm tra trạng thái hiện tại có phải trạng thái đích hay không ?
    def is_goal(self):    
       return self.data in State.Problem_Instance.get_goal_states() 