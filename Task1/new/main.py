from ManhattanHeuristic import ManhattanDistanceHeuristic
import AStarSearch
import Problem
from EightPuzzleProblem import EightPuzzleProblem

# Define the initial state for the Eight Puzzle Problem
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Example initial state
problem = EightPuzzleProblem(initial_state)

heuristic = ManhattanDistanceHeuristic()
astar = AStarSearch(heuristic.h)
solution = astar.search(problem)
print("Solution:", solution)