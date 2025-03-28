import random
import copy

def generate(n):
    res = []
    for i in range(n):
        b = []
        for k in range(16):
            b.append(random.randint(1, 16))
        res.append(b)
    return res

def mutations():
    return random.randint(0, 15), random.randint(1, 16)

def mutate(population, mutations):
    i, j = mutations()
    population[i] = j
    return population

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

def crossover(x, y):
    i, j = random.randint(0, 15), random.randint(0, 15)
    if (j < i):
        i, j = j, i
    a = copy.deepcopy(x)
    a[i:j+1] = y[i:j+1]
    return a

def geneticAlgorithm(p, fn):
    best = 0
    for sth in range(100):
        new_p = []
        potentials = [fn(ind) for ind in p]
        for k in range(len(p)):
            x, y = random.choices(p, weights=potentials, k=2)
            child = crossover(x, y)
            child = mutate(child, mutations)
            a = fn(child)
            if a == 120:
                return child
            if a > best:
                best = a
                print(sth, a)
            new_p.append(child)
        p = new_p
    return p

#p = [1,3,5,2,13,9,14,12,15,6,16,7,4,11,8,10], [1,3,5,7,9,11,13,15,16,14,12,10,8,6,4,2]
p = generate(1024)
res = geneticAlgorithm(p, fn)
