from Heuristic import Heuristic
from Visual import Visual
import Node 
import State
import Problem
from Searching import Searching

#Set the goal state for problem
goal_states = []
goal_states.append(State.State([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
goal_states.append(State.State([[8, 7, 6], [5, 4, 3], [2, 1, 0]]))
goal_states.append(State.State([[0, 8, 7], [6, 5, 4], [3, 2, 1]]))
goal_states.append(State.State([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))


#Set the inital state for problem
initial_state = State.State([
    [1, 3, 5],
    [2, 4, 0],
    [6, 7, 8]
])


#Set the problem
EightPuzzleProblem = Problem.Problem(initial_state, goal_states)

#Test the visual 
#demo_node = Node.Node(initial_state)
#dot = Visual.graph_search(demo_node, 100)
#dot.view()

#print the Heuristic
H1 = Heuristic("EnhancedManhattan")
H2 = Heuristic("EnhancedMissplace")
value1 = H1.getHeuristic(initial_state, EightPuzzleProblem.get_goal_states())
value2 = H2.getHeuristic(initial_state, EightPuzzleProblem.get_goal_states())

#Demo A* and path of A*
search1 = Searching(H1)
search2 = Searching(H2)

path_of_search1 = search1.AStar(EightPuzzleProblem)
path_of_search2 = search2.AStar(EightPuzzleProblem)

#actions_of_search1 = path_of_search1[1]
#print(actions_of_search1)
#for path in path_of_search1[0]:
    #print(f"State: \n{path}\n g_value: {path.pathCost}, h_value: {path.H_1}")

#actions_of_search2 = path_of_search2[1]
#print(actions_of_search2)
#for path in path_of_search2[0]:
    #print(f"State: \n{path}\n g_value: {path.pathCost}, h_value: {path.H_1}")

search1.Visual()
search2.Visual()
