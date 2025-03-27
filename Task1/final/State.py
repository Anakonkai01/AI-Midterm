import copy

class State():
    def __init__(self, board):
        self.board = board # 

    def __eq__(self, other): # 
        return self.board == other.board

    def __hash__(self): # 
        return hash(str(self.board))

    def __str__(self):
        return str(self.board)

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_blank_position(self): # return position of blank cell
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def swap(self, pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2
        self.board[i1][j1], self.board[i2][j2] = self.board[i2][j2], self.board[i1][j1]

    
    def getActions(self): # return all possible actions
        actions = []
        blank_position = self.get_blank_position()
        if blank_position[0] > 0:
            actions.append('U')
        if blank_position[0] < 2:
            actions.append('D')
        if blank_position[1] > 0:
            actions.append('L')
        if blank_position[1] < 2:
            actions.append('R')
        return actions

    def getCost(self, state, action):
        return 1

    def getSuccessor(self, action):
        blank_position = self.get_blank_position()
        new_state = copy.deepcopy(self)

        if 'U' == action:
            new_state.swap(blank_position, (blank_position[0] - 1, blank_position[1]))
        elif 'D' == action:
            new_state.swap(blank_position, (blank_position[0] + 1, blank_position[1]))
        elif 'L' == action:
            new_state.swap(blank_position, (blank_position[0], blank_position[1] - 1))
        elif 'R' == action: 
            new_state.swap(blank_position, (blank_position[0], blank_position[1] + 1))

        # apply the auto swap rule
        new_state.auto_swap_if_adjacency()
        return new_state


    def are_adjacent(self, pos1, pos2):
        # check if two positions are adjacent (Manhattan distance = 1)
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

    def auto_swap_if_adjacency(self):
        """check if cell 1 and cell 3 are adjacent, swap them if true"""
        """check if cell 2 and cell 4 are adjacent, swap them if true"""
        
        position = {} # using dictionary to store position of each number in the board
        for i in range(3):
            for j in range(3):
                position[self.board[i][j]] = (i, j)

        # swap if cell 1 and cell 3 are adjacent
        if self.are_adjacent(position[1], position[3]):
            self.swap(position[1], position[3])

        # swap if cell 2 and cell 4 are adjacent
        if self.are_adjacent(position[2], position[4]):
            self.swap(position[2], position[4])
