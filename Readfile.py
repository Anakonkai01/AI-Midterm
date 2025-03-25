import matplotlib.pyplot as plt

def readfile(filename):
    wall = set()
    food = set()
    pie = set()
    corner = dict()
    start = None

    with open(filename, 'r') as f:
        lines = f.readlines()
        
        height = len(lines)  # height of the maze
        width = len(lines[0].strip())  # width of the maze

        for x, line in enumerate(lines):
            for y, char in enumerate(line.strip()):
                if char == '%':
                    wall.add((x, y))
                elif char == '.':
                    food.add((x, y))
                elif char == 'P':
                    start = (x, y)
                elif char == 'O':
                    pie.add((x, y))
        
        corner["top_left_left"] = (0, 1)
        corner["top_left_top"] = (1, 0)

        corner["top_right_top"] = (1, width - 1)
        corner["top_right_right"] = (0, width - 2)

        corner["bot_left_left"] = (height - 1, 1)
        corner["bot_left_bot"] = (height - 2, 0)

        corner["bot_right_right"] = (height - 1, width - 2)
        corner["bot_right_bot"] = (height - 2, width - 1)

    return wall, food, pie, start, corner

def find_neigbour(graph, x, y):
    neigbours = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    result = []
    for neigbour in neigbours:
        if not graph.is_wall(*neigbour):
            result.append(neigbour)
    return result


def del_food(graph, x, y):
    if (x, y) in graph.food:
        graph.food.remove((x, y))
    return graph

def is_all_food(graph):
    return len(graph.food) == 0





