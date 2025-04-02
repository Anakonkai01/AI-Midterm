import graphviz as g
class Node: # TODO: need to do something with this class because it not done 
    def __init__(self, state, action = None, parent = None, pathCost =None, H_1=None):
        self.state = state 
        self.action = action #hành động tạo nên node đó
        self.parent = parent #node cha sinh ra node hiện tại
        self.pathCost = pathCost #số hành động để từ nguồn sinh ra node hiện tại
        self.H_1 = H_1
        self.ID = str(state)

    def __str__(self):
        return  '\n'.join(''.join(str(num) if num != 0 else '_' for num in row) for row in self.get_state())

    def __lt__(self, other):
        return self.pathCost + self.H_1 < other.pathCost + other.H_1

    def get_state(self):
        return self.state
    
    def get_action(self):
        return self.action
    
    def get_path_cost(self):
        return self.pathCost

    def get_parent(self):
        return self.parent

    def get_id(self):
        return self.ID

    #For visualize 
    def get_str_node(self):
        return str(self)

    #Draw a node and its edge which is associated with its parent
    def draw(self, dot):
        dot.node(self.get_id(), self.get_str_node(),shape = "square")
        if self.get_parent() is not None:
            dot.edge(self.get_parent().get_id(), self.get_id, self.get_action())
    