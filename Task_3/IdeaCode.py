import random

def generate(n):
    res = []
    for i in range(n):
        res.append(random.sample(range(1,17), 16))
    return res

def mutate(p, rate):
        for i in range(16):
            if random.random() < rate:
                j = random.randrange(16)
                p[i], p[j] = p[j], p[i]
        return p

def random_selection(p, n):
    tournament = random.sample(p, n)
    return max(tournament, key=lambda ind: fn(ind))

def fn(p):
    row = [0]*16
    up_cross = [0]*31
    down_cross = [0]*31
    count = 0
    for i in range(16):
        count += row[p[i]-1]
        count += up_cross[(p[i]-1) + i]
        count += down_cross[(p[i]-1) - i + 15]
        row[p[i]-1] += 1
        up_cross[(p[i]-1) + i] += 1
        down_cross[(p[i]-1) - i + 15] += 1
    return 120 - count

def crossover_ox(parent1, parent2):
    size = len(parent1)
    i = random.randint(0, size - 2)
    j = random.randint(i + 1, size - 1)
    child = [-1] * size
    child[i:j+1] = parent1[i:j+1]
    pos = (j + 1) % size
    p2_index = (j + 1) % size
    while -1 in child:
        if parent2[p2_index] not in child:
            child[pos] = parent2[p2_index]
            pos = (pos + 1) % size
        p2_index = (p2_index + 1) % size
    return child

def geneticAlgorithm(p, fn):
    best = 0
    for i in range(10000):
        new_p = []
        for k in range(len(p)):
            x = random_selection(p, 5)
            y = random_selection(p, 5)
            child = crossover_ox(x, y)
            child = mutate(child, 0.1)
            a = fn(child)
            if a == 120:
                return child, 120
            if a > best:
                best = a
            new_p.append(child)
        #print("Gen:",i+1,"-Best fit:",best)
        p = new_p
    return p, best

#p = [1,3,5,2,13,9,14,12,15,6,16,7,4,11,8,10]
# for i in range(10):
#     population = generate(100)
#     res, best_fitness = geneticAlgorithm(population, fn)
#     print("----- Attemp:", i+1,)
#     if (best_fitness == 120):
#         print("Result:",res)
#     else:
#         print("Best fitness:", best_fitness)
# population = generate(100)
# res, best_fitness = geneticAlgorithm(population, fn)

print(fn([10, 3, 5, 15, 8, 6, 14, 1, 13, 7, 16, 4, 12, 9, 11, 2,]))
