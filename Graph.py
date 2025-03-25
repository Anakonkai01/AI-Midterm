def __init__(self, wall, food, pie, corner, start):
        self.wall = wall
        self.food = food
        self.pie = pie
        self.corner = corner
        self.start = start
        self.rows = max(x for x, y in wall) + 1
        self.cols = max(y for x, y in wall) + 1
        
def is_wall(self, x, y):
    if x < 0 or y < 0 or x >= self.rows or y >= self.cols or (x, y) in self.wall:
        return True
    return False

def is_food(self, x, y):
    if (x, y) in self.food:
        return True
    return False

def is_pie(self, x, y):
    if (x, y) in self.pie:
        return True
    return False

def is_corner(self, x, y):
    if (x, y) in self.corner.values():
        return True
    return False


