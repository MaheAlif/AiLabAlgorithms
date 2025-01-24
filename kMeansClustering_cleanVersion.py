import numpy as np
import matplotlib.pyplot as plt

# Loading the data into the array
dataPath = 'Algorithms/filtered_soc_with_sl.csv'
data = np.loadtxt(dataPath, delimiter=",", dtype=str, skiprows=1)

# Convert the data to float for calculation
data = data.astype(float)

# Display the data shape and type
print(type(data))
print(data.shape)

# Converting data
x = data[:, 0]  # Student ID on x-axis
y = data[:, 1]  # Mid(30) on y-axis

# defining size of graph
plt.figure(figsize=(10, 8)) 
# Create the scatter plot of original data
plt.scatter(x, y, label="Data Points")

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Student ID vs Mid(30)")

# Selecting random data points (centroids) for initial centers
k = 7
random_indices = np.random.choice(data.shape[0], k, replace=False)
centers = data[random_indices]

# Store the initial centers for later use
centers_initial = centers.copy()

# Define a colormap for the clusters and assign unique colors to them
colors = plt.cm.get_cmap('tab10', k)  # 'tab10' supports up to 10 clusters
cluster_colors = [colors(i) for i in range(k)]


# Plot the initial centers in a distinct color (red 'X' for visibility)
plt.scatter(centers_initial[:, 0], centers_initial[:, 1], color="red", label="Initial Centers", marker="x", s=100)

# Initialize the 2D list for clusters
Clusters = [[] for _ in range(k)]

# Assign each data point to the nearest cluster based on distance
for s in data:
    x3, y3 = s[0], s[1]
    distances = [np.sqrt((y3 - centers[i][1])**2 + (x3 - centers[i][0])**2) for i in range(k)]
    nearest_center_idx = np.argmin(distances)
    Clusters[nearest_center_idx].append(s)

# Convert clusters to NumPy arrays for easier plotting
Clusters = [np.array(cluster) for cluster in Clusters]

# Scatter plot the clusters with dynamic colors
for idx, cluster in enumerate(Clusters):
    if cluster.size > 0:
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}", color=cluster_colors[idx])

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Clusters with Initial Centers")
plt.legend()
plt.show()

# Calculate mean for each cluster and update centers
means = []
for idx, cluster in enumerate(Clusters):
    if cluster.size > 0:
        mean_x = np.mean(cluster[:, 0])
        mean_y = np.mean(cluster[:, 1])
        means.append([mean_x, mean_y])

# Convert means to a NumPy array for plotting
means = np.array(means)

plt.figure(figsize=(10, 8)) 
# Plot the updated means along with the clusters
for idx, cluster in enumerate(Clusters):
    if cluster.size > 0:
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {idx + 1}", color=cluster_colors[idx])

# Plot the initial centers
plt.scatter(centers_initial[:, 0], centers_initial[:, 1], color="red", label="Initial Centers", marker="x", s=100)

# Plot the updated means with the same color as the cluster they belong to
for idx, mean in enumerate(means):
    plt.scatter(mean[0], mean[1], color=cluster_colors[idx], label=f"Updated Mean {idx + 1}", marker="o", s=100)

# Add labels and title
plt.xlabel("Student ID")
plt.ylabel("Mid(30) Score")
plt.title("Scatter Plot of Clusters with Updated Means")
plt.legend()
plt.show()

# Flag for iterative updating of centers
flag = True
itr = 0

while True:
    # Recalculate means and reassign clusters based on updated centroids
    new_clusters = [[] for _ in range(k)]
    for s in data:
        x3, y3 = s[0], s[1]
        distances = [np.sqrt((y3 - mean[1])**2 + (x3 - mean[0])**2) for mean in means]
        nearest_center_idx = np.argmin(distances)
        new_clusters[nearest_center_idx].append(s)

    # Convert new clusters to NumPy arrays
    new_clusters = [np.array(cluster) for cluster in new_clusters]

    # Update the means
    new_means = []
    for cluster in new_clusters:
        if cluster.size > 0:
            mean_x = np.mean(cluster[:, 0])
            mean_y = np.mean(cluster[:, 1])
            new_means.append([mean_x, mean_y])

    # Check if the means have changed
    if np.array_equal(means, new_means):
        print("The means are the same. Ending the loop.")
        flag = False
    else:
        print(f"The means are different. Continuing iteration -> ",itr)
        means = np.array(new_means)
        itr+=1

    
    if flag == False :
        plt.figure(figsize=(10, 8))
        # Plot the clusters, updated centers, and means
        for idx, cluster in enumerate(new_clusters):
            if cluster.size > 0:
                plt.scatter(cluster[:, 0], cluster[:, 1], color=cluster_colors[idx])

        # Plot the initial centers and updated means with the same color
        plt.scatter(centers_initial[:, 0], centers_initial[:, 1], color="red", label="Initial Centers", marker="x", s=100)
        
        # Plot the updated means with the same color as the cluster they belong to
        for idx, mean in enumerate(means):
            plt.scatter(mean[0], mean[1], color=cluster_colors[idx], marker="o", s=100, edgecolor='black', linewidth=2, label=f"Updated Mean {idx + 1}")

        # Add labels and title
        plt.xlabel("Student ID")
        plt.ylabel("Mid(30) Score")
        plt.title("Scatter Plot of Updated Clusters with Means")
        plt.legend()
        plt.show()
        break

    # Optionally, you can add the condition to break the loop if the means are stable.
