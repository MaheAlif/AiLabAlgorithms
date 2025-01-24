import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def total_distance(route, points):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(points[route[i] - 1], points[route[i + 1] - 1])
    return distance


def hill_climbing(points):
    n = len(points)
    current_route = list(range(1, n + 1)) + [1]  
    current_distance = total_distance(current_route, points)

    while True:
        best_neighbor = None
        best_distance = current_distance

        
        for i in range(1, n):
            for j in range(i + 1, n):
                neighbor = current_route[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor_distance = total_distance(neighbor, points)

                if neighbor_distance < best_distance:
                    best_neighbor = neighbor
                    best_distance = neighbor_distance

        
        if best_distance >= current_distance:
            break

        
        current_route = best_neighbor
        current_distance = best_distance

    return current_route, current_distance


n = (input())
points = []
for i in range(1, int(n)+1):
    x, y = map(float, input().split())
    points.append((x, y))

route, total_distance = hill_climbing(points)
print(f"Route: {' -> '.join(str(i) for i in route)}")
print(f"Total Distance: {total_distance:.2f}")