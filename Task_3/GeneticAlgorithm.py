import random
import copy

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

def random_selection(p, n, fn):
    a = random.choices(p, k=n)
    if (fn(a[0]) > fn(a[1])):
        a[0], a[1] = a[1], a[0]
    for i in a:
        if fn(i) > fn(a[0]):
            a[0] = i
        elif fn(i) > fn(a[1]):
            a[1] = i
    return a[1], a[0]

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
    for i in range(10000):
        new_p = []
        potentials = [fn(ind) for ind in p]
        for k in range(len(p)):
            x, y = random_selection(p, 5, fn)
            child = crossover(x, y)
            child = mutate(child, 0.1)
            a = fn(child)
            if a == 120:
                print(a)
                return child
            if a > best:
                best = a
            new_p.append(child)
        p = new_p
    return p

# p = [1,3,5,2,13,9,14,12,15,6,16,7,4,11,8,10]
population = generate(100)
res = geneticAlgorithm(population, fn)
print(res)

