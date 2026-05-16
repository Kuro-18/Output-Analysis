import numpy as np

num_replications = 5
warmup = 20

results = []

for r in range(num_replications):

    # Simulated data
    data = np.random.normal(50, 5, 100)

    # Artificial warm-up effect
    data[:20] -= 15

    # Delete warm-up period
    steady_state = data[warmup:]

    # Compute average
    avg = np.mean(steady_state)

    results.append(avg)

overall_mean = np.mean(results)

print("Replication Means:")
print(results)

print("\nOverall Mean:")
print(overall_mean)