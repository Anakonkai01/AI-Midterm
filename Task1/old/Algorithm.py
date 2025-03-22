import heapq
from Node import Node
from Tools import Tools
class Algorithm: 
# A* với Enhanced heuristic
    def A_Star(initial_state_node, goal_state_nodes):

        frontier = []
        priority_H = min(initial_state_node.get_H_EM())
        heapq.heappush(frontier,(priority_H, initial_state_node))
        cost_path = 0
        cos_so_far = {initial_state_node:0}
        explored = set()

        while frontier:
            node = heapq.heappop(frontier)

            #Kiểm tra xem phải trạng thái đích ?
            if node.get_state().is_goal():
                return  
            
            explored.add(node.get_state())

            if isinstance(node,Node):
            #Duyệt qua các successors của đỉnh hiện tại
                for successor in node.get_successors(): 
                    # Lấy giá trị H nhỏ nhất của đỉnh hiện tại so với các đỉnh đích
                    current_H_of_node = min(successor.get_H_EM())
                    #Tính chi phí đường đi từ đỉnh nguồn tới đỉnh hiện tại 
                    







