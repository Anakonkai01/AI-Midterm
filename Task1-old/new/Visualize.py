import graphviz as g
class Visualize:
    @staticmethod 
    def graph_search(node, problem, max_num_nodes = 20):
        dot = g.Digraph()
        frontier = list()
        explored = set() #set
        frontier.append(node) #queue
        count = 0

        while len(frontier) > 0 and count < max_num_nodes:
            current_node = frontier.pop(0) # remove node from frontier
            current_node.draw(dot)
            count = count + 1
            explored.add(current_node)# add current node to explored set
            successors = problem.getSuccessors(current_node.get_state())
            for successor in successors:
                if successor.get_state() not in [node.get_state() for node in frontier] and successor.get_state() not in [node.get_state() for node in explored]: # Lỗi nếu so sánh trực tiếp ID vì có trường hợp trùng state nhưng khác ID
                    frontier.append(successor)# expand the successor of current node to frontier if only ...
        return dot