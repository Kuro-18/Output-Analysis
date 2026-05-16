import numpy as np
import matplotlib.pyplot as plt

# Example simulation outputs from 5 replications
replications = []

for r in range(5):
    # Simulated noisy data approaching steady state
    data = np.random.normal(loc=50, scale=5, size=100)
    data[:20] -= np.linspace(20, 0, 20)
    replications.append(data)

replications = np.array(replications)

# Average across replications
average_output = np.mean(replications, axis=0)

# Moving average smoothing
window = 5
smoothed = np.convolve(
    average_output,
    np.ones(window)/window,
    mode='valid'
)

# Plot
plt.plot(average_output, label="Average Output")
plt.plot(smoothed, label="Welch Smoothed", linewidth=3)
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.title("Welch Method")
plt.show()