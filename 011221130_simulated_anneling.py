import math
import random

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def total_distance(route, points):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(points[route[i] - 1], points[route[i + 1] - 1])
    return distance

def simulated_annealing(points, initial_temperature, cooling_rate):
    n = len(points)
    current_route = list(range(1, n + 1)) + [1]
    current_distance = total_distance(current_route, points)

    best_route = current_route[:]
    best_distance = current_distance

    temperature = initial_temperature
    it = 0

    while (temperature >= 1):
        i = int(random.uniform(1,5))
        j = int(random.uniform(1,5))
        # print(f"\nI : {i} & J : {j}")
        if i == j:
            continue
        
        new_route = current_route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_distance = total_distance(new_route, points)

        delta = new_distance - current_distance
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_route = new_route
            current_distance = new_distance

            if current_distance < best_distance:
                best_route = current_route[:]
                best_distance = current_distance

        temperature *= cooling_rate
        # print(f"temp : {temperature}\n")
        print(f"In iteration {it + 1}: Best Distance = {best_distance:.2f}")
        it = it+1

    return best_route, best_distance

# Start of code
# n = input("Enter the number of points :")
# n = int(n)
# points = []
# for i in range(1,n+1):
#     for j in range(1,2):
#         x,y = input(f"Enter the x and y of point-{i}: ").split()
#         points.append( ( float(x) , float(y) ) )

points = [(0.0, 0.0), (2.0, 3.0), (4.0, 0.0), (4.0, 3.0), (6.0, 1.0)]

initial_temperature = 1000
cooling_rate = 0.7

# calling Simulated Annealing
route, distance = simulated_annealing(points, initial_temperature, cooling_rate)
print(f"\nRoute: {' -> '.join(str(i) for i in route)}")
print(f"Total Distance: {distance:.2f}")
