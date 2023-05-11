from window import window
import random, time

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def randomPoint():
    return point(random.randint(0,1000), random.randint(0,1000))

def dist(u, v):
    return ( (u.x-v.x)**2 + (u.y-v.y)**2 )**0.5

def desirability(u, v, phermone_strenght):
    return ((1/(dist(u,v))) ** 4) * phermone_strenght ** 1

def render_points(points):
    for p in points:
        w.circle(p.x, p.y, 5)

def render_path(path):
    for i in range(len(path)):
        u = points[path[i]]
        v = points[path[(i+1)%len(path)]]
        w.line(u.x, u.y, v.x, v.y)
        w.update()
        time.sleep(0.1)

def findPath(first, phermones, numberOfCities):
    curr = first
    vist = [False] * numberOfCities
    vist[curr] = True
    moves = [curr]
    total_dist = 0
    for i in range(numberOfCities-1):
        weights = []
        for j in range(numberOfCities):
            if vist[j]:
                weights.append(0)
            else:
                weights.append(desirability(points[curr], points[j], phermones[curr][j]))
        choices = [ i for i in range(0, numberOfCities) ]
        v = random.choices(choices, weights)[0]
        moves.append(v)
        vist[v] = True
        total_dist = total_dist + dist(points[curr], points[v])
        curr = v
    total_dist = total_dist + dist(points[curr], points[first])
    return [moves, total_dist]

#Initialize How many Ants we have exploring
numberOfAnts = 20

#Number of times we want the algorithm to run for
maxIterations = 1000

#How many Cities need to be explored
numberOfCities = 10 

points = []

w = window()
for i in range(numberOfCities):
    points.append(randomPoint())

phermones = []

for i in range(numberOfCities):
    phermones.append([1]*numberOfCities)


best_dist = 1e17
best_path = []
for j in range(maxIterations):
    change = False
    for i in range(numberOfAnts):
        m = findPath(random.randint(0,numberOfCities-1), phermones, numberOfCities)
        if m[1] < best_dist:
            best_dist = m[1]
            best_path = m[0]
            change = True

    for i in range(numberOfCities):
        for j in range(numberOfCities):
            phermones[i][j] = max(1, phermones[i][j] * 0.75)
    
    for i in range(numberOfCities):
        u = best_path[i]
        v = best_path[(i+1)%numberOfCities]
        phermones[u][v] = 10
    
    if change:
        w.clear()
        render_points(points)
        render_path(best_path)
        w.update()
        time.sleep(1)
        print("Best Distance:", best_dist)

print("Ended Iterations")

w.keep()
