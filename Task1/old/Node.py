from graphviz import Digraph as dg
from Problem import Problem
from Tools import Tools
from Node import Node
from State import State
import copy as cp
class Node:

    # Khởi tạo 1 đối tượng trong Problem để lấy các goal state(dùng cho mục đích tính các giá trị Heuristic)
    Problem_Instance = Problem()

    #Hàm khởi tạo các thuộc tính của 1 đỉnh
    def __init__(self, state=State, action= None, parent = None):
        self.state = state 
        self.action = action 
        self.parent = parent 
        self.ID = str(self)
        self.H_EM = [Tools.Enhanced_Manhattan_distance_heuristic(self.state, goal) for goal in Node.State.Problem_instance.get_goal_states()] #Heuristic với Enhanced Manhattan 
        self.H_MP= [Tools.Missplace_heuristic(self.state, goal) for goal in Node.Problem_instance.get_goal_states()] #Heuristics với Misplace Cell
        self.G = 1 #Chi phí thực để đến được 1 trạng thái (tất cả đều giống nhau 1 bước di chuyển)



    #Trạng thái của đỉnh được biểu diễn dưới dạng chuỗi để vẽ trong graphviz
    def __str__(self):         
        return "\n".join(" ".join(str(title) if title != 0 else '_' for title in row) for row in self.state.get_data())


    #
    def get_successors(self):
        actions = ['L', 'R', 'U', 'D']
        successors = []
        for action in actions:
            current_state = cp.deepcopy(self.state.get_matrix())
            successor_state = self.get_successor(current_state, action) #Tạo ra các successor tương ứng với đỉnh hiện tại
            if successor_state is not None:
                successors.append(Node(successor_state, action, self)) #Chỉ lấy các successor  
        return successors

    # Hàm sử dụng để tính 1 successor cho 1 hành động 
    def get_successor(self, state_data, action):
        X_blank, Y_blank = self.get_blank_pos(state_data)
        X, Y = self.get_des_pos(action, X_blank, Y_blank)  # X, Y là vị trí mới của ô trống
        if 0 <= X < 3 and 0 <= Y < 3:
            state_data[X_blank][Y_blank], state_data[X][Y] = state_data[X][Y], state_data[X_blank][Y_blank]  # Di chuyển khoảng trống ứng với hành động (đổi chỗ ô trống với ô mà nó có thể đến được)
            self.check_and_swap(state_data, X_blank, Y_blank) #X_blank,Y_blank lúc này lại có giá trị của X,Y do vừa đổi
            return state_data
        return None


    def get_des_pos(self, action, X, Y):# Trả về vị trí ô trống có thể tới với 1 hành động
        if action == 'L':  
            Y += 1        # Ô này là ô nằm phía bên phải của khoảng trống -> d/c sang trái 
        if action == 'R':
            Y -= 1        # Ô này là ô nằm phía bên trái của khoảng trống -> d/c sang phải
        if action == 'D':  
            X += 1        # Ô này là ô nằm phía bên trên của khoảng trống -> d/c xuống
        if action == 'U':
            X -= 1        # Ô này là ô nằm phía bên dưới của khoảng trống -> d/c lên
        return X,Y


    #Trả về vị trí của ô trống
    def get_blank_pos(self, state_data): 
        return next((X,Y) for X in range(len(state_data)) for Y in range(len(state_data[X])) if state_data[X][Y] == 0)


    #Kiểm tra điều kiện & đổi chỗ ô 1 với ô 3 và ô 2 với ô 4 nếu thấy chúng kề nhau 
    def check_and_swap(self, state_data, X, Y):
        groups = [(2, 4), (1, 3)]
        for pair in groups:
            print(state_data[X][Y])
            if state_data[X][Y] in pair:
                neighbors = [(X, Y - 1), (X, Y + 1), (X + 1, Y), (X - 1, Y)]
                for dx, dy in neighbors:
                    # Kiểm tra tọa độ hợp lệ trước khi đổi
                    if 0 <= dx < len(state_data) and 0 <= dy < len(state_data[0]):
                        if state_data[dx][dy] in pair and state_data[dx][dy] != state_data[X][Y]:
                            # Swap hai ô
                            state_data[X][Y], state_data[dx][dy] = state_data[dx][dy], state_data[X][Y]
                            return  # Chỉ swap 1 lần và thoát luôn

                       
    #Khởi tạo 1 đồ thị
    dot = dg()

    #Lấy ID của node
    def get_id(self):
        return self.ID

    #Lấy state có trong node
    def get_str_node(self):
        return str(self)


    #Lấy hành động tạo nên node đó
    def get_action(self):
        return self.action 


    #
    def get_H_EM(self):
        return self.H_EM

    def get_H_MP(self):
        return self.H_MP
    

    def get_G(self):
        return self.G

    def get_state(self):
        return self.state

    #Vẽ đỉnh hiện tại cùng với cạnh nối với đỉnh cha của nó
    def draw(self, dot):
        dot.node(self.get_id(), self.get_str_node(),shape = 'square')
        if self.parent is not None:
            dot.edge(self.parent.get_id(),self.get_id(), self.get_action())

    # Vẽ các successor  của đỉnh hiện tại
    def draw_successors(self, dot, node=Node):
        succesors = node.get_successors() 
        for succesor in succesors:
            self.draw(dot)

        