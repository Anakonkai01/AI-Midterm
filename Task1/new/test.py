import EightPuzzleProblem
import graphviz as g
import Visualize
import Node
import EightPuzzleState
import EightPuzzleProblem

board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]


#Kiểm tra hàm get_successor() trả về các node chứ không phải state
test_state =   EightPuzzleState.EightPuzzleState(board)
prob = EightPuzzleProblem.EightPuzzleProblem([],[])
demo_node = Node.Node(board)
Visual = Visualize.Visualize()
dot = Visual.graph_search(demo_node,prob, 10000)
dot
#successors = prob.getSuccessors(test_state)

#for node in successors:
    #if isinstance(node, Node.Node):
        #parent = node.get_parent()
        #print(f"Parent: {parent.get_state()}\n Action: {node.get_action()}")
        #print(node.get_state())
        #print()

