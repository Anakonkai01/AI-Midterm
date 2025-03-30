import heapq
import math
from Graph import Graph

def heuristic(position, graph):
    # tinh kc manhattan
    def manhattan_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    x, y, food, pie, step = position

    if not food:
        return 0
    # tinh kc den cac goc co thuc an
    # duyet qua all corners va giu lai cac corners co food
    corner_distances = [manhattan_distance((x, y), corner) for corner in graph.corners if corner in food]

    # uoc luong so buoc it nhat de den duoc food o corner gan nhat + them it nhat 1 buoc cho cac food con lai
    if corner_distances:
        return min(corner_distances) + len(food) - 1
    # neu khong co food o corner thi tra ve kc manhattan giua food xa nhat va pacman roi + them it nhat 1 buoc cho cac food con lai
    return max(manhattan_distance((x, y), f) for f in food) + (len(food) - 1)

def find_neighbours(position, graph):
    # x, y la toa do cua pacman
    # food la tap hop food chua an
    # pie la tap hop cac banh ma thuat
    # step la so magic step con lai
    x, y, food, pie, step = position 

    # dinh nghia cac huong di chuyen cua pacman
    directions = [(0, 1, 'South'), (1, 0, 'East'), (0, -1, 'North'), (-1, 0, 'West')]
    

    for dx, dy, action in directions:
        # tinh vi tri moi cua pacman
        nr, nc = x + dx, y + dy
        
        # Kiem tra xem pacman con o trong me cung khong
        if nr < 0 or nr >= graph.rows or nc < 0 or nc >= graph.cols:
            continue

        # giam so buoc magic xuong 1
        new_step = max(0, step - 1) 

        # Neu gap tuong va khong co magic step thi khong di huong do
        if graph.is_wall((nr, nc)) and new_step == 0:
            continue
        
        # tao bien danh dau teleport
        teleport_used = False
        teleport_food = None
        # thiet lap vi tri moi 
        new_x, new_y = nr, nc
        # tao ban sao cua tap food
        new_food = food.copy()
        
        # check neu nr, nc la entrance cua goc
        if (nr, nc) in graph.corners:
            # danh dau bien teleport
            teleport_used = True
            # ghi nho vi tri entrance cua teleport
            teleport_food = (nr, nc)
            # loai bo food o entrance neu co
            if (nr, nc) in new_food:
                new_food = new_food - frozenset({(nr, nc)})
            # thuc hien tele den vi tri destination
            new_x, new_y = graph.corners[(nr, nc)]
            # neu destination la wall va khong co magic step thi bo qua huong di
            if graph.is_wall((new_x, new_y)) and new_step == 0:
                continue
            # loai bo food o destination neu co
            if (new_x, new_y) in new_food:
                new_food = new_food - frozenset({(new_x, new_y)})
        else:
            # neu khong phai la corner thi kiem tra va loai bo food o vi tri do
            if (new_x, new_y) in new_food:
                new_food = new_food - frozenset({(new_x, new_y)})
        
        # cap nhat lai tap hop pie
        new_pie = pie.copy()
        if (new_x, new_y) in new_pie:
            new_pie = new_pie - frozenset({(new_x, new_y)})
            new_step = 5  # dat lai magic step neu nhat duoc pie
        # giam chi phi de uu tien su dung teleport
        extra_cost = 0.5 if teleport_used else 1
        
        # tra ve trang thai moi 
        yield (new_x, new_y, frozenset(new_food), frozenset(new_pie), new_step), action, extra_cost, teleport_food


def astar_search(graph):
    start_state = (graph.start[0], graph.start[1], frozenset(graph.food), frozenset(graph.pie), 0)
    frontier = [(heuristic(start_state, graph), 0, start_state)]
    came_from = {start_state: (None, None)}
    cost_so_far = {start_state: 0}
    
    while frontier:
        f, g, state = heapq.heappop(frontier)
        if cost_so_far[state] > g:
            continue
        
        x, y, food, pie, step = state
        if not food:
            path = []
            while state in came_from and came_from[state][0] is not None:
                state, action = came_from[state]
                path.append(action)
            return path[::-1], cost_so_far[state]
        
        for next_state, action, cost,_ in find_neighbours(state, graph):
            new_cost = cost_so_far[state] + cost
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + heuristic(next_state, graph)
                heapq.heappush(frontier, (priority, new_cost, next_state))
                came_from[next_state] = (state, action)
    
    return None, None

def apply_action(state, action, graph):
    """
    Từ state hiện tại và hành động action, trả về trạng thái kế tiếp.
    Duyệt qua các trạng thái hàng xóm được tạo bởi find_neighbours, nếu action trùng khớp,
    trả về trạng thái đó. Nếu không tìm thấy, trả về state ban đầu.
    """
    for next_state, act, cost, teleportFood in find_neighbours(state, graph):
        # 
        if act == action:
            return next_state, teleportFood
    return state, None

def remove_eaten(graph, position):
    """
    Cập nhật đồ thị bằng cách xóa điểm thức ăn và bánh ma thuật tại vị trí đã ăn.
    Input:
        graph: đối tượng Graph chứa danh sách các điểm food và pie.
        position: tuple (x, y) vị trí Pacman đã đến (đã ăn nếu có).
    Output:
        Đồ thị được cập nhật (graph.food và graph.pie đã loại bỏ vị trí đó nếu có).
    """
    if position in graph.food:
        graph.food.remove(position)
    if position in graph.pie:
        graph.pie.remove(position)
    return graph
