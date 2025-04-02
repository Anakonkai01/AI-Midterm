import heapq
from Node import Node
from Problem import Problem
from Heuristic import Heuristic
import graphviz as g
import uuid
class Searching:
    def __init__(self,heuristic: Heuristic):
        self.uniqueId = str(uuid.uuid4())[:8] #Id cho file hình ảnh
        self.heuristic = heuristic
        self.graph = g.Digraph(name = f"Graph_{self.uniqueId}")

    def AStar(self, problem: Problem):

        initial_state = problem.get_initial_state()
        if problem.isGoalState(initial_state):
            return []

        initial_H  = self.heuristic.heuristic_func(initial_state, problem.get_goal_states())
        initial_node = Node(initial_state,H_1=initial_H, pathCost=0)

        frontier = []
        heapq.heappush(frontier, initial_node)

        explored = {initial_node.get_state() : 0}

        while frontier:
            node = heapq.heappop(frontier)
            node.draw(self.graph)
            if problem.isGoalState(node.get_state()):
                return self.getPath(node)

            for successor in node.getSuccessors():
                stateOfSuccessor = successor.get_state()
                g_value = node.pathCost + successor.getCost()#Chi phí hiện tại của cha + chi phí đến con
                h_value = self.heuristic.heuristic_func(stateOfSuccessor, problem.get_goal_states())
                # Không tính f(x) = g(x) + h(x) vì đã định nghĩa phương thức __lt__ trong node để tự động so sánh


                if stateOfSuccessor not in explored or g_value < explored[stateOfSuccessor]:
                    explored[stateOfSuccessor] = g_value
                    successor.set_G(g_value)
                    successor.set_H(h_value)
                    successor.set_parent(node)
                    heapq.heappush(frontier, successor)

        return None



    def getPath(self, node):
        path = []
        actions = []
        while node:
            path.append(node)
            actions.append(node.get_action())
            if isinstance(node, Node):
                node = node.get_parent()
        return path[::-1], actions


    def Visual(self):
        self.graph.view()

