# unsupervised learning practice

# unsupervised learning = learning from unlabeled data
# the algorithm finds hidden patterns on its own

# key techniques:
# clustering -> group similar items (k-means, hierarchical, dbscan)
# dimensionality reduction -> reduce features (pca, t-sne)
# association rules -> find item relationships (apriori)

# k-means steps:
# 1. choose k (number of clusters)
# 2. initialize k random centroids
# 3. assign each point to nearest centroid
# 4. recalculate centroids (mean of assigned points)
# 5. repeat 3-4 until convergence

import numpy as np
import matplotlib.pyplot as plt


# k-means from scratch
def kmeans(data, k, max_iterations=100):
    np.random.seed(42)

    # randomly pick k points as initial centroids
    indices = np.random.choice(len(data), k, replace=False)
    centroids = data[indices].copy()

    for iteration in range(max_iterations):
        # assign each point to nearest centroid
        distances = np.zeros((len(data), k))
        for i in range(k):
            distances[:, i] = np.sqrt(np.sum((data - centroids[i]) ** 2, axis=1))
        labels = np.argmin(distances, axis=1)

        # recalculate centroids
        new_centroids = np.zeros_like(centroids)
        for i in range(k):
            cluster_points = data[labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = cluster_points.mean(axis=0)

        # check if converged
        if np.allclose(centroids, new_centroids):
            print(f"  converged at iteration {iteration + 1}")
            break

        centroids = new_centroids

    return centroids, labels


# generating sample data with 3 clusters
np.random.seed(42)
cluster1 = np.random.randn(30, 2) + [2, 2]
cluster2 = np.random.randn(30, 2) + [8, 3]
cluster3 = np.random.randn(30, 2) + [5, 8]
data = np.vstack([cluster1, cluster2, cluster3])

print(f"total data points: {len(data)}")
print(f"clustering into k=3 groups...\n")

centroids, labels = kmeans(data, k=3)

print(f"\nfinal centroids:")
for i, centroid in enumerate(centroids):
    count = np.sum(labels == i)
    print(f"  cluster {i + 1}: center=({centroid[0]:.2f}, {centroid[1]:.2f}), points={count}")

# plotting
colors = ["#e74c3c", "#3498db", "#2ecc71"]
plt.figure(figsize=(8, 6))
for i in range(3):
    cluster_data = data[labels == i]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1],
                c=colors[i], s=50, alpha=0.7, label=f"cluster {i + 1}")
plt.scatter(centroids[:, 0], centroids[:, 1],
            c="black", s=200, marker="X", linewidths=2, label="centroids")
plt.title("k-means clustering result")
plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# elbow method to find best k
def calculate_wcss(data, k):
    centroids, labels = kmeans(data, k)
    wcss = 0
    for i in range(k):
        cluster_points = data[labels == i]
        wcss += np.sum((cluster_points - centroids[i]) ** 2)
    return wcss

print("\nelbow method:")
k_values = range(1, 8)
wcss_values = []
for k in k_values:
    wcss = calculate_wcss(data, k)
    wcss_values.append(wcss)
    print(f"  k={k}: wcss = {wcss:.2f}")

plt.figure(figsize=(8, 5))
plt.plot(list(k_values), wcss_values, marker="o", linewidth=2, color="#e74c3c")
plt.axvline(x=3, color="#3498db", linestyle="--", label="optimal k=3")
plt.title("elbow method for optimal k")
plt.xlabel("number of clusters (k)")
plt.ylabel("wcss")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# simple pca
print("\npca - dimensionality reduction")

np.random.seed(42)
data_3d = np.random.randn(100, 3)
data_3d[:, 1] = data_3d[:, 0] * 0.7 + np.random.randn(100) * 0.3
data_3d[:, 2] = data_3d[:, 0] * 0.3 + np.random.randn(100) * 0.5

print(f"original data shape: {data_3d.shape}")

# standardize
mean = data_3d.mean(axis=0)
std = data_3d.std(axis=0)
data_std = (data_3d - mean) / std

# covariance matrix
cov_matrix = np.cov(data_std.T)
print(f"\ncovariance matrix:\n{np.round(cov_matrix, 3)}")

# eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print(f"\neigenvalues: {np.round(eigenvalues, 3)}")

# sort by eigenvalue
sorted_idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_idx]
eigenvectors = eigenvectors[:, sorted_idx]

# explained variance
total_variance = eigenvalues.sum()
explained_variance = eigenvalues / total_variance * 100
print(f"\nexplained variance:")
for i, (ev, var) in enumerate(zip(eigenvalues, explained_variance)):
    print(f"  pc{i + 1}: eigenvalue={ev:.3f}, variance={var:.1f}%")

# reduce to 2d
data_2d = data_std @ eigenvectors[:, :2]
print(f"\nreduced data shape: {data_2d.shape}")

plt.figure(figsize=(8, 5))
plt.scatter(data_2d[:, 0], data_2d[:, 1], c="#3498db", alpha=0.6, s=40)
plt.title("pca: 3d to 2d projection")
plt.xlabel(f"pc1 ({explained_variance[0]:.1f}% variance)")
plt.ylabel(f"pc2 ({explained_variance[1]:.1f}% variance)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
