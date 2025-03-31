from Graph import Graph
from Search import astar_search, apply_action, remove_eaten
import pygame 
import time

# Đọc dữ liệu từ file
wall, food, pie, start = Graph.readfile("task02_pacman_example_map.txt")
graph = Graph(wall, food, pie, start)
path, cost = astar_search(graph)

# Tính toán kích thước màn hình dựa trên kích thước đồ thị
num_rows = max(y for _, y in graph.wall + graph.food + graph.pie) + 1
num_cols = max(x for x, _ in graph.wall + graph.food + graph.pie) + 1
cell_width = 30
cell_height = 30
WIDTH = num_cols * cell_width
HEIGHT = num_rows * cell_height

# Cấu hình hiển thị bằng pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Pathfinding ")
fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

def draw_graph(graph, pacman_pos):
    # Vẽ tường
    for x, y in graph.wall:
        pygame.draw.rect(screen, (0, 0, 255), (x * cell_width, y * cell_height, cell_width, cell_height))
    # Vẽ thức ăn (ô trắng)
    for x, y in graph.food:
        pygame.draw.rect(screen, (255, 255, 255), (x * cell_width, y * cell_height, cell_width, cell_height))
    # Vẽ bánh ma thuật (ô vàng)
    for x, y in graph.pie:
        pygame.draw.rect(screen, (255, 255, 0), (x * cell_width, y * cell_height, cell_width, cell_height))
    # Vẽ Pacman
    pac_x, pac_y = pacman_pos
    pygame.draw.circle(screen, (255, 0, 0), (pac_x * cell_width + cell_width // 2, pac_y * cell_height + cell_height // 2), min(cell_width, cell_height) // 3)


# Thay vì sử dụng vector di chuyển đơn giản, ta sử dụng trạng thái được tính từ A*
# Khởi tạo trạng thái ban đầu (không có magic, với tập food và pie ban đầu)
current_state = (graph.start[0], graph.start[1], frozenset(graph.food), frozenset(graph.pie), 0)
# Lưu chuỗi các trạng thái dựa trên danh sách hành động từ A*
state_sequence = [(current_state, None)]
for action in path:
    current_state, teleportfood = apply_action(current_state, action, graph)
    state_sequence.append((current_state, teleportfood))

# Vòng lặp mô phỏng di chuyển của Pacman
index = 0
move_delay = 0.3  # thời gian delay giữa các bước
last_move_time = time.time()
if path:
    print("Actions:", ", ".join(path))
    print("Total cost:", len(path))
else:
    print("No path found")
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if index < len(state_sequence) and (time.time() - last_move_time) >= move_delay:
        current_state, teleportfood = state_sequence[index]
        index += 1
        last_move_time = time.time()
        # Cập nhật đồ thị: xóa các ô thức ăn và bánh ma thuật nếu Pacman đã đi qua
        pacman_pos = (current_state[0], current_state[1])
        if teleportfood is not None:
            graph = remove_eaten(graph, teleportfood)
        graph = remove_eaten(graph, pacman_pos)

    screen.fill((0, 0, 0))
    # Dùng vị trí Pacman từ current_state để vẽ
    draw_graph(graph, (current_state[0], current_state[1]))
    pygame.display.flip()

pygame.quit()
