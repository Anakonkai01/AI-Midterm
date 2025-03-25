from Node import Node
import Search


class BFS_Search(Search.Search):
    def __init__(self):
        pass   



    def search(self, problem):
        initial_state = problem.getInitialState()
        if problem.isGoalState(initial_state):
            return []
        
        frontier = []
        explored = set()
        initial_node = Node(initial_state, None, None, 0,0)
        frontier.append(initial_node)

        while frontier:
            node = frontier.pop(0)

            if problem.isGoalState(node.state):
                return self.getPath(node)
            
            explored.add(node.ID)
            for new_state, action, cost in problem.getSuccessors(node.state):
                new_node = Node(new_state, action, node, node.pathCost + cost,0)
                if new_node.ID not in explored:
                    frontier.append(new_node)
        return "No solution"
    
    def getPath(self, node):
        path = []
        while node.parent:
            path.insert(0, node.action)
            node = node.parent
        return path
    
    def getLength(self, node):
        length = 0
        while node.parent:
            length += 1
            node = node.parent
        return length