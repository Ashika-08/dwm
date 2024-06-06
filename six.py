import math

# Points
points = {
    "A": (2, 2),
    "B": (3, 2),
    "C": (1, 1),
    "D": (3, 1),
    "E": (1.5, 0.5)
}

# Initial cluster centers
centroids = {
    "Cluster1": (2, 2),
    "Cluster2": (1, 1)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to assign clusters
def assign_clusters(points, centroids):
    clusters = {key: [] for key in centroids}
    for point_id, point in points.items():
        closest_centroid = min(centroids, key=lambda c: euclidean_distance(point, centroids[c]))
        clusters[closest_centroid].append(point)
    return clusters

# Function to update centroids
def update_centroids(clusters):
    new_centroids = {}
    for cluster_id, cluster_points in clusters.items():
        mean_x = sum(p[0] for p in cluster_points) / len(cluster_points)
        mean_y = sum(p[1] for p in cluster_points) / len(cluster_points)
        new_centroids[cluster_id] = (mean_x, mean_y)
    return new_centroids

# K-means clustering function
def kmeans(points, centroids, max_iterations=100):
    for _ in range(max_iterations):
        clusters = assign_clusters(points, centroids)
        new_centroids = update_centroids(clusters)

        # Convergence check
        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters, centroids

# Run K-means algorithm
clusters, final_centroids = kmeans(points, centroids)

# Print the results
print("Clusters:")
for cluster_id, cluster_points in clusters.items():
    print(f"{cluster_id}: {cluster_points}")

print("\nFinal Centroids:")
for centroid_id, centroid in final_centroids.items():
    print(f"{centroid_id}: {centroid}")
