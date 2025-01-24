import numpy as np
import matplotlib.pyplot as plt
# loading the data into the arrray!
dataPath = 'Algorithms/filtered_soc_with_sl.csv'
data = np.loadtxt(dataPath, delimiter=",", dtype=str, skiprows=1)

# Convert the NumPy array to a Python list
# data_list = data.tolist()

for x in data:
    print(x)
print(type(data))
print(data.shape)

# Converting data
x = data[:, 0].astype(float)  # Student ID on x-axis
y = data[:, 1].astype(float)  # Mid(30) on y-axis

# Create the scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Student ID vs Mid(30)")
# plt.show()


# Selecting random datapoints from the dataset
# Randomly select k rows
k=4
fixed_means = []
random_indices = np.random.choice(data.shape[0], k, replace=False)  # `replace=False` ensures no repetition
centers = data[random_indices]

# converting data and centers's values into float
data = data.astype(float)
centers = centers.astype(float)
# print(type(data),type(centers))

print("Randomly selected data points:")
print(centers)

# Initialize the 2D list
Clusters = [[] for _ in range(k)]

# Print the initialized Clusters list
print("Initialized Clusters:")
print(Clusters)
print(centers[0][0])  # x1
print(centers[0][1])  # y1
print(centers[1][0])  # x2
print(centers[1][1])  # y2
print(data[5][0])     # x3
print(data[5][1])     # y3
# sqrt((y3 - y1)^2 + (x3 -x1)^2 ) is the distance of (x3, y3) and (x1, y1)
# sqrt((y3 - y2)^2 + (x3 -x2)^2 ) is the distance of (x3, y3) and (x2, y2)
# Accessing coordinates
x1, y1 = centers[0][0], centers[0][1]
x2, y2 = centers[1][0], centers[1][1]


i=0
for s in data:
    x3, y3 = data[i][0], data[i][1]
    # Calculating distances
    distance_1 = np.sqrt((y3 - y1)**2 + (x3 - x1)**2)
    distance_2 = np.sqrt((y3 - y2)**2 + (x3 - x2)**2)

    # Print distances
    # print(f"Distance between (x3, y3) and (x1, y1): {distance_1}")
    # print(f"Distance between (x3, y3) and (x2, y2): {distance_2}")
    
    if distance_1 > distance_2 :
        Clusters[1].append(s)
    else :
        Clusters[0].append(s)    
    i+=1


# m = Clusters[:, 0].astype(float)  # Student ID on x-axis
# n = Clusters[:, 1].astype(float)
# Converting Clusters to NumPy arrays for easier plotting
Clusters = [np.array(cluster) for cluster in Clusters if len(cluster) > 0] 

# Scatter plot the clusters
for idx, cluster in enumerate(Clusters):
    if cluster.size > 0:  # Check if the cluster has data before plotting
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}")

# Plot the centers
plt.scatter(centers[:, 0], centers[:, 1],color="red", label="Centers", marker="x", s=100)

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Clusters")
plt.legend()
plt.show()

# Calculate mean for each cluster
means = []
for cluster in Clusters:
    mean_x = np.mean(cluster[:, 0])
    mean_y = np.mean(cluster[:, 1])
    means.append([mean_x, mean_y])

# Convert means to a NumPy array for plotting
means = np.array(means)
fixed_means = means
# for x in means:
#     print(f"Means : \n",x)

# Scatter plot the clusters
for idx, cluster in enumerate(Clusters):
    if cluster.size > 0:  # Check if the cluster has data before plotting
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}")

# Plot the centers
plt.scatter(centers[:, 0], centers[:, 1], color="red", label="Initial Centers", marker="x", s=100)

# Plot the means
plt.scatter(means[:, 0], means[:, 1], color="green", label="Cluster Means", marker="o", s=100)

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Clusters with Means")
plt.legend()
plt.show()
flag = True

while flag :
    means = []
    for cluster in Clusters:
        mean_x = np.mean(cluster[:, 0])
        mean_y = np.mean(cluster[:, 1])
        means.append([mean_x, mean_y])

    # Convert means to a NumPy array for plotting
    means = np.array(means)
    fixed_means = means
    print(means)

    # Scatter plot the clusters
    for idx, cluster in enumerate(Clusters):
        if cluster.size > 0:  # Check if the cluster has data before plotting
            plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}")

    # Plot the centers
    plt.scatter(centers[:, 0], centers[:, 1], color="red", label="Initial Centers", marker="x", s=100)

    # Plot the means
    plt.scatter(means[:, 0], means[:, 1], color="green", label="Cluster Means", marker="o", s=100)

    # Add labels and title
    plt.xlabel("Student ID")
    plt.ylabel("Mid(30) Score")
    if flag : 
         plt.title("Scatter Plot of Clusters with Means...")
    else :
         plt.title("Scatter Plot of Clusters with Means -> Final")
    plt.legend()
    plt.show()
    
    for x in means:
        if np.array_equal(fixed_means, means):
            print("The means are the same.")
            flag = False
        else:
            print("The means are different.")
