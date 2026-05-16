import numpy as np

# Long simulation run
data = np.random.normal(50, 5, 1000)

batch_size = 100
num_batches = len(data) // batch_size

batch_means = []

for i in range(num_batches):

    start = i * batch_size
    end = start + batch_size

    batch = data[start:end]

    batch_mean = np.mean(batch)

    batch_means.append(batch_mean)

print("Batch Means:")
print(batch_means)

print("\nEstimated Overall Mean:")
print(np.mean(batch_means))