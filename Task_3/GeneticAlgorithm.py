import random

class Board: 
    def __init__(self, queens_placement=[0]*16):
        self.queens_placement = queens_placement
        self.size = len(queens_placement)

    def __str__(self):
        res = ""
        for i in self.queens_placement:
            res += str(i)+" "
        return "["+res[0:len(res)-1]+"]"
    
    def getQueensPlacement(self):
        return self.queens_placement
    
    def setQueensPlacement(self, new_placement):
        self.queens_placement = new_placement

    @staticmethod
    def fitness_evaluate(board: 'Board'):
        row = [0]*16
        up_cross = [0]*31
        down_cross = [0]*31
        count = 0
        placement = board.getQueensPlacement()

        for i in range(16):
            count += row[placement[i]-1]
            count += up_cross[(placement[i]-1) + i]
            count += down_cross[(placement[i]-1) - i + 15]
            row[placement[i]-1] += 1
            up_cross[(placement[i]-1) + i] += 1
            down_cross[(placement[i]-1) - i + 15] += 1

        return 120 - count
    
    @staticmethod
    def crossover(board1: 'Board', board2: 'Board'):
        placement1 = board1.getQueensPlacement()
        placement2 = board2.getQueensPlacement()
        size = len(placement1)
        i = random.randint(0, size-2)
        j = random.randint(i+1, size-1)
        new_placement = [-1]*size
        new_placement[i:j+1] = placement1[i:j+1]
        pos = (j+1) % size
        p2_index = (j+1) % size

        while -1 in new_placement:
            if placement2[p2_index] not in new_placement:
                new_placement[pos] = placement2[p2_index]
                pos = (pos + 1) % size
            p2_index = (p2_index + 1) % size

        return Board(new_placement)

    @staticmethod
    def mutate(board: 'Board'):
        placement = board.getQueensPlacement()
        size = len(placement)
        i, j = random.randrange(size), random.randrange(size)
        placement[i], placement[j] = placement[j], placement[i]
        board.setQueensPlacement(placement)
        return board

class Population:
    def __init__(self, individuals, fitness_function, crossover_function, mutate_function):
        self.individuals = individuals
        self.fitness_function = fitness_function
        self.crossover_function = crossover_function
        self.mutate_function = mutate_function

    def getIndividuals(self):
        return self.individuals
    
    def setIndividuals(self, new_individuals):
        self.individuals = new_individuals

    def randomTournamentSelection(self, tournament_size):
        tournament = random.sample(self.getIndividuals(), tournament_size)
        return max(tournament, key=self.fitness)
    
    def crossover(self, ind1, ind2):
        return self.crossover_function(ind1, ind2)
    
    def mutate(self, ind):
        return self.mutate_function(ind)
    
    def fitness(self, ind):
        return self.fitness_function(ind)

class GeneticAlgorithm:
    def run(population: Population, population_size, max_fitness = 120, generation = 1000, mutation_rate = 0.1, tournament_size = 5):
        i = 0
        best = 0
        while (i < generation):
            new_individuals = []
            for k in range(population_size):
                parent1 = population.randomTournamentSelection(tournament_size)
                parent2= population.randomTournamentSelection(tournament_size)
                child = population.crossover(parent1, parent2)
                if random.random() < mutation_rate:
                    child = population.mutate(child)
                child_fit = population.fitness(child)
                if child_fit > best:
                    best = child_fit
                if child_fit == max_fitness:
                    print("_Gen:",i+1,"-Best fitness:", best)
                    return child
                new_individuals.append(child)
            if (i+1)%50 == 0:
                print("_Gen:",i+1+"-Best fitness:",best)
            population.setIndividuals(new_individuals)

#Generate first generation
def generate_boards(n):
    boards = []
    for i in range(n):
        temp = Board(random.sample(range(1, 17), 16))
        boards.append(temp)
    return boards

#Testing the code
sample = generate_boards(10)
p = Population(sample, fitness_function=Board.fitness_evaluate, crossover_function=Board.crossover, mutate_function=Board.mutate)
algo = GeneticAlgorithm.run(p, len(sample), max_fitness=120, generation = 1000, mutation_rate = 0.1, tournament_size = 5)
print("Here comes the result:", algo)