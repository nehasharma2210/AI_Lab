import numpy as np
import pandas as pd
import time

# Load data
data = pd.read_csv("cities.csv")
X = data.values

k = 3


# ===================== GRADIENT DESCENT =====================
start_time = time.time()

centroids_gd = X[np.random.choice(len(X), k, replace=False)]
alpha = 0.01
iterations_gd = 50

for _ in range(iterations_gd):
    clusters = [[] for _ in range(k)]

    for x in X:
        distances = [np.linalg.norm(x - c) for c in centroids_gd]
        cluster = np.argmin(distances)
        clusters[cluster].append(x)

    for i in range(k):
        if clusters[i]:
            grad = sum([2*(centroids_gd[i] - x) for x in clusters[i]])
            centroids_gd[i] = centroids_gd[i] - alpha * grad

# SSD calculation
ssd_gd = sum(np.linalg.norm(x - centroids_gd[i])**2
             for i in range(k) for x in clusters[i])

time_gd = time.time() - start_time


# ===================== NEWTON METHOD =====================
start_time = time.time()

centroids_nm = X[np.random.choice(len(X), k, replace=False)]
iterations_nm = 10

for _ in range(iterations_nm):
    clusters = [[] for _ in range(k)]

    for x in X:
        distances = [np.linalg.norm(x - c) for c in centroids_nm]
        cluster = np.argmin(distances)
        clusters[cluster].append(x)

    for i in range(k):
        if clusters[i]:
            centroids_nm[i] = np.mean(clusters[i], axis=0)

# SSD calculation
ssd_nm = sum(np.linalg.norm(x - centroids_nm[i])**2
             for i in range(k) for x in clusters[i])

time_nm = time.time() - start_time


# ===================== OUTPUT =====================

print("\n========== FINAL COMPARISON ==========\n")

print("Gradient Descent Results:")
print("Centroids:\n", centroids_gd)
print("Iterations:", iterations_gd)
print("SSD:", ssd_gd)
print("Time Taken:", round(time_gd, 5), "seconds\n")

print("Newton Method Results:")
print("Centroids:\n", centroids_nm)
print("Iterations:", iterations_nm)
print("SSD:", ssd_nm)
print("Time Taken:", round(time_nm, 5), "seconds\n")


# Comparison Summary
print("========== SUMMARY ==========\n")

if ssd_nm < ssd_gd:
    print("Newton Method gives better clustering (lower SSD)")
else:
    print("Gradient Descent gives better clustering")

if time_nm < time_gd:
    print("Newton Method is faster")
else:
    print("Gradient Descent is faster")