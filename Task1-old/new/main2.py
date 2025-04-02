import random
import BFS_Search
import EightPuzzleProblem
import EightPuzzleState
import AStarSearch
import MisplacesTilesHeuristic
import ManhattanHeuristic

def generate_test_cases(seed=69, hard_cases=10, random_cases=20):
    random.seed(seed)
    hard_test_cases = []
    random_test_cases = []
    
    # Generate hard test cases with multiple swaps between 1,3 and 2,4
    for _ in range(hard_cases):
        state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Start from goal state
        for _ in range(random.randint(15, 25)):  # Apply 15-25 swaps
            i, j = random.choice([(0, 0), (0, 1), (1, 0), (1, 1)])
            state[i][j], state[i][j+1] = state[i][j+1], state[i][j]  # Swap horizontally
            state[i][j], state[i+1][j] = state[i+1][j], state[i][j]  # Swap vertically
        hard_test_cases.append(state)
    
    # Generate completely random test cases
    for _ in range(random_cases):
        numbers = list(range(9))
        random.shuffle(numbers)
        state = [numbers[:3], numbers[3:6], numbers[6:]]
        random_test_cases.append(state)
    
    return hard_test_cases, random_test_cases

hard_cases, random_cases = generate_test_cases()

test_cases = {f"Hard_test_case_{i+1}": case for i, case in enumerate(hard_cases)}
test_cases.update({f"Random_test_case_{i+1}": case for i, case in enumerate(random_cases)})

goal_states = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
    [[8, 7, 6], [5, 4, 3], [2, 1, 0]],
    [[0, 8, 7], [6, 5, 4], [3, 2, 1]],
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
]
goal_states = tuple(EightPuzzleState.EightPuzzleState(state) for state in goal_states)


def run_search(search_algorithm, heuristic_name, file_name):
    """Hàm chạy tìm kiếm và lưu kết quả vào file"""
    with open(file_name, "w") as file:
        for test_name, test_case in test_cases.items():
            problem_instance = EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case), goal_states)
            result = search_algorithm.search(problem_instance)
            actions = result
            file.write(f"{test_name}:\nActions: {actions}\nNumber of actions: {len(actions)}\n\n")
            print(f"{test_name}: Actions: {actions}\nNumber of actions: {len(actions)}\n")


# Chạy BFS
bfs = BFS_Search.BFS_Search()
run_search(bfs, "BFS", "bfs_results.txt")

# Chạy A* với Manhattan heuristic
#a_star_manhattan = AStarSearch.AStarSearch(ManhattanHeuristic.ManhattanHeuristic())
#run_search(a_star_manhattan, "A* Manhattan", "a_star_results_manhattan.txt")

# Chạy A* với Misplaced Tiles heuristic
#a_star_misplaced = AStarSearch.AStarSearch(MisplacesTilesHeuristic.MisplacesTilesHeuristic())
#run_search(a_star_misplaced, "A* Misplaced Tiles", "a_star_results_misplaced_tiles.txt")
