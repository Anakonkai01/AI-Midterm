import pygame
import time
from Graph import Graph
from Search import Search
from Visualize import Visualize

# Step 1: Read data from file and create a Graph object
graph = Graph.readfile("task02_pacman_example_map.txt")

# Step 2: Initialize the Search object with the graph
search = Search(graph, graph.start)

# Step 3: Perform A* search to find the optimal path
path, cost = search.astar_search()

# Step 4: Initialize visualization class with the graph
visualize = Visualize(graph)

# Step 5: Simulate the path with Pac-Man's movements
current_state = (graph.start[0], graph.start[1], frozenset(graph.food), frozenset(graph.pie), 0)
state_sequence = [(current_state, None)]
for action in path:
    current_state, teleportfood = search.apply_action(current_state, action)
    state_sequence.append((current_state, teleportfood))

# Initialize simulation variables
index = 0
move_delay = 0.01  # Delay between each move
last_move_time = time.time()
if path:
    print("Actions:", ", ".join(path))
    print("Total cost:", len(path))
    print("\nHeuristic values at each step:")
    for state, _ in state_sequence:
        h_value = search.heuristic(state, graph)
        print(f"State: {state[:2]}, Heuristic: {h_value}")
else:
    print("No path found")
visited_positions = []

start_screen = True  # Flag to show the start screen message
animation_started = False  # Flag to track whether the animation has started

# Step 7: Main visualization loop
run = True
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Check if any key is pressed to start the game (after pressing any key, start animation)
        if event.type == pygame.KEYDOWN and start_screen and not animation_started:
            animation_started = True  # Set flag to True once animation starts
            start_screen = False  # Remove the start screen message
    
    if start_screen:
        # Display the start screen message
        visualize.screen.fill((0, 0, 0))  # Fill screen with black
        font = pygame.font.SysFont("verdana", 32)
        text = font.render("Press any key to Start", True, (255, 255, 255))
        visualize.screen.blit(text, (visualize.WIDTH // 2 - text.get_width() // 2, visualize.HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        continue  # Skip the rest of the loop and wait for key press to start the animation
    
    # Make Pac-Man move step by step along the path
    if index < len(state_sequence) and (time.time() - last_move_time) >= move_delay:
        current_state, teleportfood = state_sequence[index]
        index += 1
        last_move_time = time.time()

        # Pac-Man's current position
        pacman_pos = (current_state[0], current_state[1])

        # Remove food from Pac-Man's current position (and teleport if applicable)
        if teleportfood is not None:
            graph = search.remove_eaten(graph, teleportfood)
        graph = search.remove_eaten(graph, pacman_pos)

        # Record the visited positions
        visited_positions.append(pacman_pos)

        # Step 8: Draw the updated state
        visualize.draw(pacman_pos, visited_positions)

# Step 9: Exit the program when finished
pygame.quit()