import csv
import math

# Points
points = {
    "A1": (2, 10),
    "A2": (2, 5),
    "A3": (8, 4),
    "A4": (5, 8),
    "A5": (7, 5),
    "A6": (6, 4),
    "A7": (1, 2),
    "A8": (4, 9)
}

# Initial cluster centers
centroids = {
    "C1": (2, 10),
    "C2": (5, 8),
    "C3": (1, 2)
}

# Save the dataset as CSV
csv_file = 'kmeans_points.csv'
csv_centroids_file = 'kmeans_centroids.csv'

# Save points to CSV
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Point', 'X', 'Y'])
        for point, coords in points.items():
            writer.writerow([point, coords[0], coords[1]])
except IOError:
    print("I/O error while saving points")

# Save centroids to CSV
try:
    with open(csv_centroids_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Centroid', 'X', 'Y'])
        for centroid, coords in centroids.items():
            writer.writerow([centroid, coords[0], coords[1]])
except IOError:
    print("I/O error while saving centroids")

# Read the dataset from CSV
def read_csv(file):
    dataset = {}
    with open(file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            dataset[row[0]] = (float(row[1]), float(row[2]))
    return dataset

points = read_csv(csv_file)
centroids = read_csv(csv_centroids_file)

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
        if cluster_points:
            mean_x = sum(p[0] for p in cluster_points) / len(cluster_points)
            mean_y = sum(p[1] for p in cluster_points) / len(cluster_points)
            new_centroids[cluster_id] = (mean_x, mean_y)
        else:
            new_centroids[cluster_id] = centroids[cluster_id]  # Keep the old centroid if no points assigned
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
