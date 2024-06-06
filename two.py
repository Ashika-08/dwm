import csv
import random
import math

# Data from the table
data = [
    [1.0, 1.0],
    [1.5, 2.0],
    [3.0, 4.0],
    [5.0, 7.0],
    [3.5, 5.0],
    [4.5, 5.0],
    [3.5, 4.5]
]

# Save the dataset as CSV
csv_file = 'kmeans_data.csv'

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])
        for row in data:
            writer.writerow(row)
except IOError:
    print("I/O error")

# Read the dataset from CSV
def read_csv(file):
    dataset = []
    with open(file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            dataset.append([float(value) for value in row])
    return dataset

data = read_csv(csv_file)

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

# Function to assign clusters
def assign_clusters(data, centroids):
    clusters = {}
    for point in data:
        closest_centroid = min(centroids, key=lambda centroid: euclidean_distance(point, centroid))
        if closest_centroid not in clusters:
            clusters[closest_centroid] = []
        clusters[closest_centroid].append(point)
    return clusters

# Function to update centroids
def update_centroids(clusters):
    new_centroids = []
    for points in clusters.values():
        new_centroid = [sum(dim) / len(points) for dim in zip(*points)]
        new_centroids.append(tuple(new_centroid))
    return new_centroids

# K-means clustering function
def kmeans(data, k, max_iterations=100):
    # Randomly initialize centroids
    centroids = random.sample(data, k)
    centroids = [tuple(centroid) for centroid in centroids]

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)

        # Convergence check
        if set(new_centroids) == set(centroids):
            break
        centroids = new_centroids

    return clusters, centroids

# Number of clusters
k = 2

# Run K-means algorithm
clusters, centroids = kmeans(data, k)

# Print the results
print("Clusters:")
for centroid, points in clusters.items():
    print(f"Centroid {centroid}: {points}")

print("\nFinal Centroids:")
for centroid in centroids:
    print(centroid)
