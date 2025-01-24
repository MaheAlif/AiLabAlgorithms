import math

# calculate mahattan distance !
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# calculate total distance of a route !
def total_distance(route, points):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(points[route[i] - 1], points[route[i + 1] - 1])
    return distance

# Hill Climbing algorithm ->
def hill_climbing(points):
    n = len(points)
    if n == 0:
        return [], 0  

    current_route = list(range(1, n + 1)) + [1]
    print(f"\nCurrent route : {current_route}")
    current_distance = total_distance(current_route, points)
    print(f"\nCurrent distance : {current_distance}")

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
                    print(f"\nCurrent best distance : {best_distance}\nCurrent best neighbour : {best_neighbor}")

        if best_distance >= current_distance:
            break

        current_route = best_neighbor
        current_distance = best_distance

    return current_route, current_distance

# start of code ->
n = input("Enter the number of points :")
n = int(n)
points = []
for i in range(1,n+1):
    for j in range(1,2):
        x,y = input(f"Enter the x and y of point-{i}: ").split()
        points.append( ( float(x) , float(y) ) )



# points = [(0.0, 0.0), (2.0, 3.0), (4.0, 0.0), (4.0, 3.0), (6.0, 1.0)]
print(f"Points : {points}")

# calling the hill climbing algorithm
if len(points):
    route, total_route_distance = hill_climbing(points)
    print(f"\nOptimized Route: {' -> '.join(str(i) for i in route)}")
    print(f"Total Distance: {total_route_distance:.2f}")
else:
    print("Insufficient valid points provided.")
