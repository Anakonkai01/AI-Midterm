import BFS_Search
import EightPuzzleProblem
import EightPuzzleState
import AStarSearch
import MisplacesTilesHeuristic
import ManhattanHeuristic

# Test Case 1: Các ô 1 và 3, 2 và 4 nằm cạnh nhau (hàng đầu tiên và thứ hai)
test_case_1 = [
    [1, 3, 5],
    [2, 4, 0],
    [6, 7, 8]
]

# Test Case 2: Ô trống ở góc trên bên trái, 1 và 3 nằm cạnh nhau ở hàng đầu tiên, 2 và 4 ở hàng thứ hai
test_case_2 = [
    [0, 1, 3],
    [2, 4, 5],
    [6, 7, 8]
]

# Test Case 3: Swap theo chiều dọc: 1 và 3, 2 và 4 nằm cạnh nhau theo chiều dọc
test_case_3 = [
    [1, 2, 5],
    [3, 4, 6],
    [0, 7, 8]
]

# Test Case 4: Một cấu hình khác với 1 và 3 nằm cạnh nhau ở hàng đầu tiên, 2 và 4 ở hàng thứ hai
test_case_4 = [
    [5, 1, 3],
    [2, 4, 6],
    [7, 8, 0]
]

hard_test_case_1 = [
    [8, 6, 7],
    [2, 5, 4],
    [3, 0, 1]
]

hard_test_case_2 = [
    [3, 1, 6],
    [4, 2, 7],
    [8, 0, 5]
]

hard_test_case_3 = [
    [4, 2, 7],
    [3, 1, 6],
    [8, 0, 5]
]
 



goal_state = []
goal_state.append(EightPuzzleState.EightPuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
goal_state.append(EightPuzzleState.EightPuzzleState([[8, 7, 6], [5, 4, 3], [2, 1, 0]]))
goal_state.append(EightPuzzleState.EightPuzzleState([[0, 8, 7], [6, 5, 4], [3, 2, 1]]))
goal_state = tuple(goal_state)



# bfs = BFS_Search.BFS_Search()

# with open("bfs_results.txt", "w") as file:
#     def run_and_log(test_case_name, problem_instance):
#         result = bfs.search(problem_instance)
#         actions = result
#         file.write(f"{test_case_name}:\n")
#         file.write(f"Actions: {actions}\n")
#         file.write(f"Number of actions: {len(actions)}\n\n")
#         print(f"{test_case_name}:")
#         print(f"Actions: {actions}")
#         print(f"Number of actions: {len(actions)}\n")

#     run_and_log("BFS with test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_1), goal_state))
#     run_and_log("BFS with test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_2), goal_state))
#     run_and_log("BFS with test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_3), goal_state))
#     run_and_log("BFS with test case 4", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_4), goal_state))
#     run_and_log("BFS with hard test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_1), goal_state))
#     run_and_log("BFS with hard test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_2), goal_state))
#     run_and_log("BFS with hard test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_3), goal_state))


# A* with Manhattan heuristic
a_star = AStarSearch.AStarSearch(ManhattanHeuristic.ManhattanHeuristic())

with open("a_star_results_manhattan.txt", "w") as file:
    def run_and_log_a_star(test_case_name, problem_instance):
        result = a_star.search(problem_instance)
        actions = result
        file.write(f"{test_case_name}:\n")
        file.write(f"Actions: {actions}\n")
        file.write(f"Number of actions: {len(actions)}\n\n")
        print(f"{test_case_name}:")
        print(f"Actions: {actions}")
        print(f"Number of actions: {len(actions)}\n")

    run_and_log_a_star("A* with test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_1), goal_state))
    run_and_log_a_star("A* with test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_2), goal_state))
    run_and_log_a_star("A* with test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_3), goal_state))
    run_and_log_a_star("A* with test case 4", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_4), goal_state))
    run_and_log_a_star("A* with hard test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_1), goal_state))
    run_and_log_a_star("A* with hard test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_2), goal_state))
    run_and_log_a_star("A* with hard test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_3), goal_state))


# A* with Misplaces Tiles heuristic
a_star = AStarSearch.AStarSearch(MisplacesTilesHeuristic.MisplacesTilesHeuristic())

with open("a_star_results_misplaced_tiles.txt", "w") as file:
    def run_and_log_a_star(test_case_name, problem_instance):
        result = a_star.search(problem_instance)
        actions = result
        file.write(f"{test_case_name}:\n")
        file.write(f"Actions: {actions}\n")
        file.write(f"Number of actions: {len(actions)}\n\n")
        print(f"{test_case_name}:")
        print(f"Actions: {actions}")
        print(f"Number of actions: {len(actions)}\n")

    run_and_log_a_star("A* with test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_1), goal_state))
    run_and_log_a_star("A* with test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_2), goal_state))
    run_and_log_a_star("A* with test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_3), goal_state))
    run_and_log_a_star("A* with test case 4", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(test_case_4), goal_state))
    run_and_log_a_star("A* with hard test case 1", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_1), goal_state))
    run_and_log_a_star("A* with hard test case 2", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_2), goal_state))
    run_and_log_a_star("A* with hard test case 3", EightPuzzleProblem.EightPuzzleProblem(EightPuzzleState.EightPuzzleState(hard_test_case_3), goal_state))