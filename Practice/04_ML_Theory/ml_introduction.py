# ml introduction - theory + practice

# types of ml:
# supervised learning   -> labeled data (input-output pairs)
# unsupervised learning -> unlabeled data (find patterns)
# reinforcement learning -> reward based learning

# supervised:
#   classification -> predict categories (spam/not spam)
#   regression -> predict continuous values (house price)

# unsupervised:
#   clustering -> group similar data (k-means)
#   dimensionality reduction -> reduce features (pca)

# reinforcement:
#   agent learns by interacting with environment
#   gets rewards/penalties for actions


import numpy as np
import matplotlib.pyplot as plt


# linear regression from scratch
print("linear regression - study hours vs marks")

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks = np.array([20, 30, 35, 50, 55, 60, 72, 78, 85, 95])

print("study hours:", study_hours)
print("marks:      ", marks)

# calculating slope and intercept
# m = sum((xi - x_mean)(yi - y_mean)) / sum((xi - x_mean)^2)
# b = y_mean - m * x_mean

n = len(study_hours)
x_mean = study_hours.mean()
y_mean = marks.mean()

numerator = np.sum((study_hours - x_mean) * (marks - y_mean))
denominator = np.sum((study_hours - x_mean) ** 2)

m = numerator / denominator
b = y_mean - m * x_mean

print(f"\nslope (m): {m:.4f}")
print(f"intercept (b): {b:.4f}")
print(f"equation: y = {m:.2f}x + {b:.2f}")

# predictions
predictions = m * study_hours + b
print("\npredictions:", np.round(predictions, 2))

# predict for new value
new_hours = 7.5
predicted_marks = m * new_hours + b
print(f"\nif study hours = {new_hours}, predicted marks = {predicted_marks:.2f}")

# r2 score
ss_res = np.sum((marks - predictions) ** 2)
ss_tot = np.sum((marks - y_mean) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print(f"r2 score: {r_squared:.4f}")

# plot
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, marks, color="#e74c3c", s=80, label="actual data", zorder=5)
plt.plot(study_hours, predictions, color="#3498db", linewidth=2, label=f"best fit: y={m:.2f}x+{b:.2f}")
plt.scatter(new_hours, predicted_marks, color="#2ecc71", s=120, marker="*",
            label=f"prediction ({new_hours}h -> {predicted_marks:.0f})", zorder=5)
plt.title("linear regression: study hours vs marks")
plt.xlabel("study hours")
plt.ylabel("marks")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# knn classifier from scratch
print("\nknn classifier - body type prediction")

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))

def knn_predict(train_data, train_labels, test_point, k=3):
    distances = []
    for i in range(len(train_data)):
        dist = euclidean_distance(train_data[i], test_point)
        distances.append((dist, train_labels[i]))

    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]

    # majority vote
    labels = [label for _, label in k_nearest]
    prediction = max(set(labels), key=labels.count)
    return prediction, k_nearest

# training data: [height(cm), weight(kg)] -> category
train_data = [
    [170, 65], [175, 70], [180, 80], [160, 55],
    [155, 50], [165, 60], [190, 90], [185, 85],
    [150, 45], [168, 62]
]
train_labels = [
    "normal", "normal", "athletic", "normal",
    "thin", "normal", "athletic", "athletic",
    "thin", "normal"
]

test_point = [172, 68]
prediction, neighbors = knn_predict(train_data, train_labels, test_point, k=3)

print(f"training data points: {len(train_data)}")
print(f"test point: height={test_point[0]}cm, weight={test_point[1]}kg")
print(f"k = 3")
print(f"\nnearest neighbors:")
for dist, label in neighbors:
    print(f"  distance: {dist:.2f} -> {label}")
print(f"\nprediction: {prediction}")
