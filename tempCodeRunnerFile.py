import numpy as np
import matplotlib.pyplot as plt

# loading the data into the array
dataPath = 'filtered_soc_with_sl.csv'
data = np.loadtxt(dataPath, delimiter=",", dtype=str, skiprows=1)

# Convert data to float
data = data.astype(float)

# Selecting random data points as centers
k = 2
random_indices = np.random.choice(data.shape[0], k, replace=False)  # `replace=False` ensures no repetition
centers = data[random_indices]

# Convert centers to float
centers = centers.astype(float)

print("Randomly selected data points as centers:")
print(centers)

# Initialize the 2D list for clusters
Clusters = [[] for _ in range(k)]

# Assign each point to the closest center
for s in data:
    x3, y3 = s[0], s[1]
    # Calculate distances to each center
    distances = [np.sqrt((y3 - center[1])**2 + (x3 - center[0])**2) for center in centers]
    closest_center = np.argmin(distances)  # Index of the closest center
    Clusters[closest_center].append(s)

# Convert Clusters to NumPy arrays for easier plotting and calculations
Clusters = [np.array(cluster) for cluster in Clusters]

# Function to calculate the mean of each cluster
def calculate_means(clusters):
    means = []
    for cluster in clusters:
        mean_x = np.mean(cluster[:, 0])
        mean_y = np.mean(cluster[:, 1])
        means.append([mean_x, mean_y])
    return np.array(means)

# Initial calculation of means
means = calculate_means(Clusters)

# Initial centers are the randomly selected points
fixed_means = np.copy(means)

# Scatter plot function for visualization
def plot_clusters():
    for idx, cluster in enumerate(Clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}")
    plt.scatter(centers[:, 0], centers[:, 1], color="red", label="Initial Centers", marker="x", s=100)
    plt.scatter(means[:, 0], means[:, 1], color="green", label="Cluster Means", marker="o", s=100)
    plt.xlabel("Student ID")
    plt.ylabel("Mid(30) Score")
    plt.title("Scatter Plot of Clusters with Means")
    plt.legend()
    plt.show()

# Run the while loop until convergence
while np.allclose(fixed_means, means, atol=1e-5) == False:  # Check if means have converged
    # Re-assign points to the new cluster centers (means)
    Clusters = [[] for _ in range(k)]
    for s in data:
        x3, y3 = s[0], s[1]
        distances = [np.sqrt((y3 - mean[1])**2 + (x3 - mean[0])**2) for mean in means]
        closest_mean = np.argmin(distances)
        Clusters[closest_mean].append(s)

    # Update the means
    fixed_means = np.copy(means)
    means = calculate_means(Clusters)

    # Plot the updated clusters
    plot_clusters()

    print(f"Updated means:\n{means}")
    print(f"Fixed means:\n{fixed_means}")
