import numpy as np
from Algorithm import Algorithm


Alg = Algorithm()
goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Current state có conflict theo hàng
current_state_row_conflict = [
        [2, 0, 3],
        [6, 5, 4],
        [8, 7, 1]
    ]

    # Current state có conflict theo cột
current_state_col_conflict = [
        [4, 5, 6],
        [1, 2, 3],
        [7, 8, 0]
    ]

goals = [
                                [[j if j != 9 else 0 for j in range(row, row + 3)] for row in range(1, 9, 3)] , # 1->8, góc phải bên dưới
                                [[j for j in range(row, row - 3, -1)] for row in range(8, -1, -3)], # 8->1, góc phải bên dưới 
                                [[j for j in range(row, row + 3)] for row in range(0, 9, 3)], # 1->8, góc trái bên trên
                                [[j if j != 9 else 0 for j in range(row, row - 3, -1)] for row in range(9, 0, -3)], # 8->1, góc trái bên trên
        ]
for goal in goals:
    print(goal)

