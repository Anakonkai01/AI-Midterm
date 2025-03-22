from graphviz import Digraph as dg
from Node import Node
class Demo:


    #Demo các thao tác với Node
        Demo_State_1 = [list(range(i, i+ 3)) for i in range(0,9,3)]
        Demo_State_2 = [[1, 4, 5],[2, 0, 3],[6, 7, 8]]

    # Demo cho việc hoán đổi vị trí & di chuyển ô trống
        #Demo_Node =Node(Demo_State_1)
        #Successors = Demo_Node.get_successors()
        #for succesor in Successors:
            #if isinstance(succesor, Node):
                #print(succesor,"\n")

    #Demo cho việc vẽ node
        #dot = dg(format='png')
        #Demo_Node_1 = Node(Demo_State_1)
        #Demo_State_2 = Node(Demo_State_2, parent=Demo_Node_1, action='L')
        #Demo_Node_1.draw_Node(dot)
        #Demo_State_2.draw_Node(dot)
        #dot.view()

    #Demo tập hợp các heuristics của 1 node với 4 trạng thái đích
        Demo_Node = Node(Demo_State_2)
        print(Demo_Node.get_H_EM())
