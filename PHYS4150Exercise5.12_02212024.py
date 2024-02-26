import numpy as np
import astropy.constants as c
import astropy.units as u

# Define the constants
h = 6.626e-34 # Planck's constant in J s
c = 3e8 # Speed of light in m/s
k = 1.381e-23 # Boltzmann's constant in J/K
T = 300 # Temperature in K

# Define the integrand function
def func(x):
    ans = x**3 / (np.exp(x) - 1)
    return ans

# Define the lower and upper limits of integration
a = 0
b = 100 # A large enough value to cover the tail of the integrand

# Define the number of subintervals
n = 100

# Define the width of each subinterval
h = (b - a) / n

# Initialize the sum
s = 0


# Loop over the subintervals
for i in range(1, n):
    # Add the value of the integrand at the midpoint of each subinterval
    s += func(a + i * h)


# Add the values of the integrand at the endpoints, weighted by 1/2
s += (func(a+0.00001) + func(b)) / 2

# Multiply the sum by the width of each subinterval
s *= h

# Multiply the result by the prefactor
s *= (k * T / h)**4 / (4 * np.pi**2 * c**2)

# Print the result
print(s)
