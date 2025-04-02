import pygame
from Graph import Graph
class Visualize:
    def __init__(self, graph, cell_size=30):
        self.graph = graph
        self.cell_size = cell_size
        self.WIDTH = graph.rows * cell_size
        self.HEIGHT = graph.cols * cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Pacman Pathfinding")

    def draw(self, pacman_pos, visited_positions=[]):
        self.screen.fill((0, 0, 0))
        for x, y in self.graph.wall:
            pygame.draw.rect(self.screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        for x, y in self.graph.food:
            pygame.draw.rect(self.screen, (255, 255, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        for x, y in self.graph.pie:
            pygame.draw.rect(self.screen, (255, 255, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        for i in range(len(visited_positions) - 1):
            pygame.draw.line(self.screen, (0, 255, 0), 
                             ((visited_positions[i][0] + 0.5) * self.cell_size, (visited_positions[i][1] + 0.5) * self.cell_size),
                             ((visited_positions[i + 1][0] + 0.5) * self.cell_size, (visited_positions[i + 1][1] + 0.5) * self.cell_size), 3)
        pygame.draw.circle(self.screen, (255, 0, 0), ((pacman_pos[0] + 0.5) * self.cell_size, (pacman_pos[1] + 0.5) * self.cell_size), self.cell_size // 3)
        pygame.display.flip()
