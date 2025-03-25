import heapq
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from copy import deepcopy

class PuzzleState:
    """
    Represents a state in the 8-puzzle problem.
    Contains the board configuration and tracks parent state and action taken.
    """
    
    def __init__(self, board, parent=None, action=None, path_cost=0):
        """
        Initialize a puzzle state with a 3x3 board configuration.
        
        Args:
            board: 2D list representing the board configuration
            parent: Parent state that led to this state
            action: Action taken to reach this state from parent
            path_cost: Cost of the path from initial state to this state
        """
        self.board = board
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.blank_position = self._find_blank_position()
        
    def _find_blank_position(self):
        """Find the position of the blank space (0) in the board."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def get_possible_actions(self):
        """Returns list of possible actions (up, down, left, right) from current state."""
        actions = []
        i, j = self.blank_position
        
        # Check up, down, left, right moves
        if i > 0:
            actions.append('up')
        if i < 2:
            actions.append('down')
        if j > 0:
            actions.append('left')
        if j < 2:
            actions.append('right')
            
        return actions
    
    def execute_action(self, action):
        """
        Execute an action and return the resulting state after applying special rules.
        
        Args:
            action: One of 'up', 'down', 'left', 'right'
            
        Returns:
            A new PuzzleState after the action and special rules are applied
        """
        i, j = self.blank_position
        new_board = deepcopy(self.board)
        
        # Move the blank space
        if action == 'up':
            new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
            new_blank = (i-1, j)
        elif action == 'down':
            new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
            new_blank = (i+1, j)
        elif action == 'left':
            new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
            new_blank = (i, j-1)
        elif action == 'right':
            new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
            new_blank = (i, j+1)
        
        # Apply special rules
        new_state = PuzzleState(new_board, self, action, self.path_cost + 1)
        self._apply_special_rules(new_state)
        
        return new_state
    
    def _apply_special_rules(self, state):
        """
        Apply the special rules to the state:
        - If cell 1 and cell 3 are adjacent, swap them
        - If cell 2 and cell 4 are adjacent, swap them
        """
        board = state.board
        
        # Find positions of cells 1, 2, 3, 4
        positions = {}
        for i in range(3):
            for j in range(3):
                if board[i][j] in [1, 2, 3, 4]:
                    positions[board[i][j]] = (i, j)
        
        # Check if cells 1 and 3 are adjacent
        if 1 in positions and 3 in positions:
            p1, p3 = positions[1], positions[3]
            if self._is_adjacent(p1, p3):
                i1, j1 = p1
                i3, j3 = p3
                board[i1][j1], board[i3][j3] = board[i3][j3], board[i1][j1]
        
        # Check if cells 2 and 4 are adjacent
        if 2 in positions and 4 in positions:
            p2, p4 = positions[2], positions[4]
            if self._is_adjacent(p2, p4):
                i2, j2 = p2
                i4, j4 = p4
                board[i2][j2], board[i4][j4] = board[i4][j4], board[i2][j2]
        
        # Update blank position if it changed
        state.blank_position = state._find_blank_position()
    
    def _is_adjacent(self, pos1, pos2):
        """Check if two positions are horizontally or vertically adjacent."""
        i1, j1 = pos1
        i2, j2 = pos2
        
        # Check horizontal adjacency
        if i1 == i2 and abs(j1 - j2) == 1:
            return True
        
        # Check vertical adjacency
        if j1 == j2 and abs(i1 - i2) == 1:
            return True
        
        return False
    
    def __eq__(self, other):
        """Two states are equal if they have the same board configuration."""
        if isinstance(other, PuzzleState):
            return self.board == other.board
        return False
    
    def __hash__(self):
        """Hash function for the state based on board configuration."""
        return hash(str(self.board))
    
    def __lt__(self, other):
        """Compare function for priority queue."""
        return self.path_cost < other.path_cost
    
    def __str__(self):
        """String representation of the board."""
        result = ""
        for row in self.board:
            result += " ".join(str(cell) if cell != 0 else "_" for cell in row) + "\n"
        return result.strip()

class EightPuzzleProblem:
    """
    Representation of the 8-puzzle problem with special rules.
    Contains the initial state and goal states.
    """
    
    # Define the 4 goal states
    GOAL_STATES = [
        [[1, 2, 3], [8, 0, 4], [7, 6, 5]],  # Goal state 1
        [[1, 2, 3], [8, 0, 4], [7, 6, 5]],  # Goal state 2
        [[3, 4, 5], [2, 0, 6], [1, 8, 7]],  # Goal state 3
        [[7, 8, 1], [6, 0, 2], [5, 4, 3]]   # Goal state 4
    ]
    
    def __init__(self, initial_state=None):
        """
        Initialize the problem with an initial state.
        If not provided, a random valid state is generated.
        """
        if initial_state:
            self.initial_state = initial_state
        else:
            self.initial_state = self._generate_random_state()
    
    def _generate_random_state(self):
        """Generate a random valid initial state."""
        # Create a flat list with numbers 0-8
        flat_board = list(range(9))
        # Shuffle the list
        random.shuffle(flat_board)
        # Convert to 3x3 board
        board = [flat_board[i:i+3] for i in range(0, 9, 3)]
        return PuzzleState(board)
    
    def is_goal(self, state):
        """Check if the current state is one of the goal states."""
        for goal in self.GOAL_STATES:
            if state.board == goal:
                return True
        return False
    
    def get_successors(self, state):
        """Generate all successor states from the current state."""
        successors = []
        actions = state.get_possible_actions()
        
        for action in actions:
            new_state = state.execute_action(action)
            successors.append(new_state)
        
        return successors

class Heuristic:
    """Class for heuristic functions used in A* search."""
    
    @staticmethod
    def manhattan_distance(state, problem):
        """
        Calculate the Manhattan distance heuristic.
        Sum of the Manhattan distances of each tile from its goal position.
        
        Args:
            state: Current puzzle state
            problem: The problem instance with goal states
            
        Returns:
            The minimum Manhattan distance to any goal state
        """
        min_distance = float('inf')
        
        for goal in problem.GOAL_STATES:
            distance = 0
            for i in range(3):
                for j in range(3):
                    if state.board[i][j] != 0:  # Skip the blank
                        # Find where this value should be in the goal
                        for gi in range(3):
                            for gj in range(3):
                                if goal[gi][gj] == state.board[i][j]:
                                    distance += abs(i - gi) + abs(j - gj)
                                    break
            min_distance = min(min_distance, distance)
        
        return min_distance
    
    @staticmethod
    def misplaced_tiles(state, problem):
        """
        Calculate the misplaced tiles heuristic.
        Count of tiles that are not in their goal position.
        
        Args:
            state: Current puzzle state
            problem: The problem instance with goal states
            
        Returns:
            The minimum number of misplaced tiles for any goal state
        """
        min_misplaced = float('inf')
        
        for goal in problem.GOAL_STATES:
            misplaced = 0
            for i in range(3):
                for j in range(3):
                    if state.board[i][j] != 0 and state.board[i][j] != goal[i][j]:
                        misplaced += 1
            min_misplaced = min(min_misplaced, misplaced)
        
        return min_misplaced

class AStar:
    """
    Implementation of the A* search algorithm for the 8-puzzle problem.
    """
    
    def __init__(self, problem, heuristic_func):
        """
        Initialize the A* search algorithm.
        
        Args:
            problem: The problem instance
            heuristic_func: The heuristic function to use
        """
        self.problem = problem
        self.heuristic_func = heuristic_func
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        
    def search(self):
        """
        Perform A* search to find a solution path.
        
        Returns:
            A solution state if found, otherwise None
        """
        start_time = time.time()
        
        # Initialize the open and closed sets
        frontier = []
        explored = set()
        
        # Calculate initial heuristic value
        initial_h = self.heuristic_func(self.problem.initial_state, self.problem)
        
        # Add initial state to frontier with f(n) = g(n) + h(n)
        heapq.heappush(frontier, (initial_h, self.problem.initial_state))
        frontier_states = {self.problem.initial_state}
        
        while frontier:
            # Track maximum frontier size
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))
            
            # Get the state with lowest f(n)
            _, current_state = heapq.heappop(frontier)
            frontier_states.remove(current_state)
            
            # Check if current state is a goal state
            if self.problem.is_goal(current_state):
                end_time = time.time()
                return {
                    'solution': current_state,
                    'nodes_expanded': self.nodes_expanded,
                    'max_frontier_size': self.max_frontier_size,
                    'time': end_time - start_time
                }
            
            # Add current state to explored set
            explored.add(current_state)
            
            # Expand current state
            self.nodes_expanded += 1
            
            for successor in self.problem.get_successors(current_state):
                if successor in explored or successor in frontier_states:
                    continue
                
                # Calculate f(n) = g(n) + h(n)
                h = self.heuristic_func(successor, self.problem)
                f = successor.path_cost + h
                
                heapq.heappush(frontier, (f, successor))
                frontier_states.add(successor)
        
        # No solution found
        end_time = time.time()
        return {
            'solution': None,
            'nodes_expanded': self.nodes_expanded,
            'max_frontier_size': self.max_frontier_size,
            'time': end_time - start_time
        }
    
    def get_solution_path(self, solution_state):
        """
        Reconstruct the solution path from initial state to goal state.
        
        Args:
            solution_state: The goal state reached
            
        Returns:
            List of states from initial to goal
        """
        path = []
        current = solution_state
        
        while current:
            path.append(current)
            current = current.parent
        
        return list(reversed(path))

class SearchTreeVisualizer:
    """
    Visualizes the search tree generated during A* search.
    """
    
    def __init__(self, max_nodes=50):
        """
        Initialize the visualizer with maximum number of nodes to display.
        
        Args:
            max_nodes: Maximum number of nodes to include in visualization
        """
        self.max_nodes = max_nodes
    
    def visualize_tree(self, solution_state):
        """
        Create a visualization of the search tree.
        
        Args:
            solution_state: The goal state reached
            
        Returns:
            A matplotlib figure of the search tree
        """
        # Get solution path
        solution_path = []
        current = solution_state
        while current:
            solution_path.append(current)
            current = current.parent
        solution_path = set(solution_path)
        
        # BFS to collect nodes for visualization
        queue = deque([solution_state])
        visited = {solution_state: 0}  # node -> level
        parent_map = {solution_state: None}
        nodes_collected = 1
        
        while queue and nodes_collected < self.max_nodes:
            current = queue.popleft()
            
            # Only process if we have a parent (skip initial state)
            if parent_map[current] is not None:
                parent = parent_map[current]
                
                # If we reached our max nodes, stop collecting
                if nodes_collected >= self.max_nodes:
                    break
                
                # Add parent->child relationship
                nodes_collected += 1
            
            # If this node has a parent, process its children
            if current.parent is not None:
                for child in self._get_children(current):
                    if child not in visited:
                        visited[child] = visited[current] + 1
                        parent_map[child] = current
                        queue.append(child)
        
        # Create nodes and edges for visualization
        node_labels = {}
        edge_labels = {}
        node_colors = []
        
        # Create graph
        import networkx as nx
        G = nx.DiGraph()
        
        # Add nodes and edges
        for node, level in visited.items():
            node_str = str(id(node))
            G.add_node(node_str)
            node_labels[node_str] = self._get_node_label(node)
            
            # Color solution path nodes differently
            if node in solution_path:
                node_colors.append('lightgreen')
            else:
                node_colors.append('lightblue')
            
            # Add edge from parent
            parent = parent_map[node]
            if parent:
                parent_str = str(id(parent))
                G.add_edge(parent_str, node_str)
                edge_labels[(parent_str, node_str)] = node.action if node.action else ""
        
        # Create visualization
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)  # positions for all nodes
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors, alpha=0.8)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, arrows=True)
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        
        plt.axis('off')
        plt.title(f"Search Tree Visualization (limited to {self.max_nodes} nodes)")
        plt.tight_layout()
        
        return plt.gcf()
    
    def _get_children(self, state):
        """Get children of a state based on parent pointer."""
        children = []
        current = state.parent
        
        # If we reached the root, return empty list
        if current is None:
            return children
        
        # The parent's parent is the grandparent
        grandparent = current.parent
        
        # If grandparent exists
        if grandparent:
            # Get all successors of grandparent
            for successor in self._get_successors(grandparent):
                if successor == current:
                    # This successor is the parent, skip
                    continue
                children.append(successor)
        
        return children
    
    def _get_successors(self, state):
        """Get all possible successors of a state."""
        successors = []
        actions = state.get_possible_actions()
        
        for action in actions:
            new_state = state.execute_action(action)
            successors.append(new_state)
        
        return successors
    
    def _get_node_label(self, state):
        """Create a compact label for a node in the visualization."""
        # Display as a flattened array with arrows for the blank
        flat = []
        for i in range(3):
            for j in range(3):
                if state.board[i][j] == 0:
                    flat.append("_")
                else:
                    flat.append(str(state.board[i][j]))
        
        return "\n".join([" ".join(flat[i:i+3]) for i in range(0, 9, 3)])

class Experiment:
    """
    Class for conducting experiments to evaluate heuristic functions.
    """
    
    def __init__(self, num_trials=50, max_depth=20):
        """
        Initialize the experiment.
        
        Args:
            num_trials: Number of random initial states to try
            max_depth: Maximum solution depth to consider
        """
        self.num_trials = num_trials
        self.max_depth = max_depth
        self.heuristics = {
            'Manhattan Distance': Heuristic.manhattan_distance,
            'Misplaced Tiles': Heuristic.misplaced_tiles
        }
    
    def run_experiment(self):
        """
        Run the experiment and return results.
        
        Returns:
            Dictionary with experiment results
        """
        results = {name: {
            'path_lengths': [],
            'nodes_expanded': [],
            'times': [],
            'success_rate': 0
        } for name in self.heuristics.keys()}
        
        for trial in range(self.num_trials):
            # Generate a random problem instance
            problem = EightPuzzleProblem()
            
            for name, heuristic_func in self.heuristics.items():
                # Run A* with the current heuristic
                astar = AStar(problem, heuristic_func)
                result = astar.search()
                
                if result['solution']:
                    # Get solution path
                    path = astar.get_solution_path(result['solution'])
                    
                    # Record results
                    results[name]['path_lengths'].append(len(path) - 1)  # Subtract 1 for initial state
                    results[name]['nodes_expanded'].append(result['nodes_expanded'])
                    results[name]['times'].append(result['time'])
                    results[name]['success_rate'] += 1
        
        # Calculate success rates and averages
        for name in self.heuristics.keys():
            results[name]['success_rate'] = (results[name]['success_rate'] / self.num_trials) * 100
            
            if results[name]['path_lengths']:
                results[name]['avg_path_length'] = sum(results[name]['path_lengths']) / len(results[name]['path_lengths'])
                results[name]['avg_nodes_expanded'] = sum(results[name]['nodes_expanded']) / len(results[name]['nodes_expanded'])
                results[name]['avg_time'] = sum(results[name]['times']) / len(results[name]['times'])
            else:
                results[name]['avg_path_length'] = 0
                results[name]['avg_nodes_expanded'] = 0
                results[name]['avg_time'] = 0
        
        return results
    
    def visualize_results(self, results):
        """
        Create visualizations of experiment results.
        
        Args:
            results: Dictionary with experiment results
            
        Returns:
            List of matplotlib figures
        """
        figures = []
        
        # Path length comparison
        plt.figure(figsize=(10, 6))
        for name in self.heuristics.keys():
            if results[name]['path_lengths']:
                plt.hist(results[name]['path_lengths'], alpha=0.5, label=name)
        plt.xlabel('Solution Path Length')
        plt.ylabel('Frequency')
        plt.title('Distribution of Solution Path Lengths')
        plt.legend()
        figures.append(plt.gcf())
        
        # Nodes expanded comparison
        plt.figure(figsize=(10, 6))
        for name in self.heuristics.keys():
            if results[name]['nodes_expanded']:
                plt.hist(results[name]['nodes_expanded'], alpha=0.5, label=name)
        plt.xlabel('Nodes Expanded')
        plt.ylabel('Frequency')
        plt.title('Distribution of Nodes Expanded')
        plt.legend()
        figures.append(plt.gcf())
        
        # Average metrics comparison
        plt.figure(figsize=(12, 6))
        names = list(self.heuristics.keys())
        metrics = ['avg_path_length', 'avg_nodes_expanded', 'avg_time']
        
        values = []
        for name in names:
            values.append([results[name][metric] for metric in metrics])
        
        x = np.arange(len(metrics))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(12, 6))
        rects1 = ax.bar(x - width/2, [values[0][i] for i in range(len(metrics))], width, label=names[0])
        rects2 = ax.bar(x + width/2, [values[1][i] for i in range(len(metrics))], width, label=names[1])
        
        ax.set_ylabel('Values')
        ax.set_title('Comparison of Average Metrics')
        ax.set_xticks(x)
        ax.set_xticklabels(['Avg Path Length', 'Avg Nodes Expanded', 'Avg Time (s)'])
        ax.legend()
        
        fig.tight_layout()
        figures.append(plt.gcf())
        
        return figures

# Main demonstration function
def main():
    # 1. Problem Formulation Demo
    print("===== 8-Puzzle Problem with Special Rules =====")
    problem = EightPuzzleProblem()
    print("Initial State:")
    print(problem.initial_state)
    print("\nGoal States:")
    for i, goal in enumerate(problem.GOAL_STATES):
        print(f"Goal {i+1}:")
        print(PuzzleState(goal))
        print()
    
    # 2. A* Search Demo with both heuristics
    print("===== A* Search with Manhattan Distance Heuristic =====")
    astar_manhattan = AStar(problem, Heuristic.manhattan_distance)
    manhattan_result = astar_manhattan.search()
    
    if manhattan_result['solution']:
        manhattan_path = astar_manhattan.get_solution_path(manhattan_result['solution'])
        print(f"Solution found in {len(manhattan_path)-1} steps!")
        print(f"Nodes expanded: {manhattan_result['nodes_expanded']}")
        print(f"Max frontier size: {manhattan_result['max_frontier_size']}")
        print(f"Search time: {manhattan_result['time']:.4f} seconds")
        
        print("\nSolution Path:")
        for i, state in enumerate(manhattan_path):
            print(f"Step {i}:")
            print(state)
            if i < len(manhattan_path) - 1:
                print(f"Action: {manhattan_path[i+1].action}")
            print()
    else:
        print("No solution found with Manhattan Distance heuristic.")
    
    print("===== A* Search with Misplaced Tiles Heuristic =====")
    astar_misplaced = AStar(problem, Heuristic.misplaced_tiles)
    misplaced_result = astar_misplaced.search()
    
    if misplaced_result['solution']:
        misplaced_path = astar_misplaced.get_solution_path(misplaced_result['solution'])
        print(f"Solution found in {len(misplaced_path)-1} steps!")
        print(f"Nodes expanded: {misplaced_result['nodes_expanded']}")
        print(f"Max frontier size: {misplaced_result['max_frontier_size']}")
        print(f"Search time: {misplaced_result['time']:.4f} seconds")
    else:
        print("No solution found with Misplaced Tiles heuristic.")
    
    # 3. Search Tree Visualization Demo
    if manhattan_result['solution']:
        print("\n===== Search Tree Visualization =====")
        visualizer = SearchTreeVisualizer(max_nodes=20)
        fig = visualizer.visualize_tree(manhattan_result['solution'])
        plt.show()
    
    # 4. Experiment Demo
    print("\n===== Heuristic Evaluation Experiment =====")
    print("Running experiment with random initial states...")
    experiment = Experiment(num_trials=20)
    results = experiment.run_experiment()
    
    print("\nExperiment Results:")
    for name, metrics in results.items():
        print(f"\n{name} Heuristic:")
        print(f"  Success Rate: {metrics['success_rate']:.1f}%")
        print(f"  Average Path Length: {metrics['avg_path_length']:.2f}")
        print(f"  Average Nodes Expanded: {metrics['avg_nodes_expanded']:.2f}")
        print(f"  Average Time: {metrics['avg_time']:.4f} seconds")
    
    # Visualize results
    figures = experiment.visualize_results(results)
    for fig in figures:
        plt.figure(fig.number)
        plt.show()

if __name__ == "__main__":
    main()