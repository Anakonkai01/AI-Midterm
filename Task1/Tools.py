import numpy as np

# Dùng để tạo các hàm tính toán phụ trợ cho Algorithm
class Tools:
    @staticmethod
    def Num_linear_conflict(current_state, goal_state):
        number_of_conflicts = 0
        look_up_conflict = lambda a,b,c: [[b,a,c], [c,b,a], [a,c,b]] #Bảng tra cứu các vị trí có thể gây xung đột để dễ dàng kiểm tra

        # Xung đột: các ô các bị đảo ngược vị trí trên cùng 1 hàng/ cột (hay còn gọi là cản trở nhau) 
        for row in range(len(current_state)): #Kiểm tra xung đột trên các hàng
            current_row = current_state[row]
            goal_row = goal_state[row] 
            a,b,c = goal_row[0], goal_row[1], goal_row[2] 
            potential_conflict_rows = look_up_conflict(a,b,c)
            if current_row in potential_conflict_rows:
                if current_row == potential_conflict_rows[1]:
                    number_of_conflicts += 2 
                    continue
                number_of_conflicts += 1
        
        for col in range(len(current_state)): #Kiểm tra xung đột trên các cột
            current_row = [current_state[row][col] for row in range(len(current_state))]
            goal_row= [goal_state[row][col] for row in range(len(goal_state))]
            a,b,c = goal_row[0], goal_row[1], goal_row[2] 
            potential_conflict_rows = look_up_conflict(a,b,c)
            if current_row in potential_conflict_rows:
                if current_row == potential_conflict_rows[1]:
                    number_of_conflicts += 2 
                    continue
                number_of_conflicts += 1
        
        return number_of_conflicts

    @staticmethod
    def Manhattan_fomula(X1,X2,Y1,Y2):
        return abs(X1-X2) + abs(Y1-Y2) 

    # Hàm Heuristic dựa trên tổng sự chêch lệch vị trí của các ô trong bàn trò chơi so với 1 kết quả
    @staticmethod
    def Manhattan_distance_heuristic(current_state, goal_state):
        sum_of_distances = 0
        for value_cell in range(1,9):
            current_cord = tuple(np.argwhere(np.array(current_state) == value_cell)[0])
            goal_cord = tuple(np.argwhere(np.array(goal_state) == value_cell)[0])
            distance_each_cell = Tools.Manhattan_fomula(current_cord[0],goal_cord[0],current_cord[1],goal_cord[1])
            #print(f"current{current_cord}   goal{goal_cord} -> distance{distance_each_cell}")
            sum_of_distances += distance_each_cell
        return sum_of_distances

    # Hàm Heuristic dựa trên tổng vị trí sai lệch so với 1 kết quả
    @staticmethod
    def Missplace_heuristic(current_state, goal_state):
        misplaced = 0 
        for row in range(3):
            for col in range(3):
                if current_state[row][col] != goal_state[row][col]:
                    misplaced += 1
        return misplaced  

    @staticmethod
    def Enhanced_Manhattan_distance_heuristic( current_state, goal_state): # Kết hợp giữa manhanttan & xung đột vị trị theo hàng/ cột (linear conflict)
        return Tools.Num_linear_conflict(current_state,goal_state) + Tools.Manhattan_distance_heuristic(current_state, goal_state) 