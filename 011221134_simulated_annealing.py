import math
import random

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(route, points):
    dist = 0
    for i in range(len(route)-1):
        dist += calculate_distance(points[route[i]], points[route[i+1]])
    return dist

def simulated_annealing(points):
    n = len(points)
    current_route = list(range(n)) + [0]
    current_distance = total_distance(current_route, points)
    
    temp = 100
    cooling_rate = 0.995
    min_temp = 0.01
    
    best_route = current_route.copy()
    best_distance = current_distance
    
    while temp > min_temp:
        new_route = current_route.copy()
        i, j = random.randint(1, n-1), random.randint(1, n-1)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        
        new_distance = total_distance(new_route, points)
        delta = new_distance - current_distance
        
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_route = new_route
            current_distance = new_distance
            
            if current_distance < best_distance:
                best_route = current_route.copy()
                best_distance = current_distance
        
        temp *= cooling_rate
    
    return best_route, best_distance

n = int(input())
points = []
for i in range(1, n+1):
    x, y = map(float, input().split())
    points.append((x, y))

best_route, best_distance = simulated_annealing(points)
print(f"Route: {' -> '.join(str(i+1) for i in best_route)}")
print(f"Total Distance: {best_distance:.2f}")