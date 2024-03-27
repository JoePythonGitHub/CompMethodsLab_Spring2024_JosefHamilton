import numpy as np
import matplotlib.pyplot as plt

# Define the function to be integrated
def f(x):
    return x**0.5/(np.exp(x) + 1)

# Sample N random numbers and evaluate the sum in the formula for the integral
N = 1_000_000
z = np.random.rand(N)
I = 2/N * np.sum(1/(np.exp(z**2) + 1))
print(I)  # Outputs

# Plot the histogram of the random numbers
plt.hist(z, bins=100, density=True)
plt.show()

# Repeat the Monte Carlo integration process multiple times
results = []
for i in range(10):
    z = np.random.rand(N)
    I = 2/N * np.sum(1/(np.exp(z**2) + 1))
    results.append(I)
print(results)