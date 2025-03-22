import Search
import Node
import heapq

class AStarSearch(Search):
    def __init__(self, heuristic):
        self.heuristic = heuristic


    def search(self, problem):
        initial_state = problem.getInitialState()
        if problem.isGoalState(initial_state):
            return []
        
        frontier = []
        explored = set()
        h_initial = self.heuristic.getHeuristic(initial_state, problem.goal_state)
        initial_node = Node(initial_state, None, None, 0, h_initial)
        heapq.heappush(frontier, initial_node)

        while frontier:
            node = heapq.heappop(frontier)

            if problem.isGoalState(node.state):
                return self.getPath(node)
            
            explored.add(node.ID)
            for new_state, action, cost in problem.getSuccessors(node.state):
                new_node = Node(new_state, node, action, node.pathCost + cost, self.heuristic.getHeuristic(new_state, problem.goal_state))
                if new_node.ID not in explored:
                    frontier.append(new_node)
        return None
    
    def getPath(self, node):
        path = []
        while node.parent:
            path.insert(0, node.action)
            node = node.parent
        return path
    
        