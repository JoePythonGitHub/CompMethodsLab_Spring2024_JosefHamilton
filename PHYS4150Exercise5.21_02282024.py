import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854e-12  # Electric constant in C²/Nm²
charge_1 = 1.0  # +1 C
charge_2 = -1.0  # -1 C
distance = 0.1  # 10 cm

# Grid dimensions
x = np.linspace(-0.5, 0.5, 101)  # 1m grid, 101 points
y = np.linspace(-0.5, 0.5, 101)  # 1m grid, 101 points

# Calculate potential at each point in the grid
potential = np.zeros((len(x), len(y)))

for i, xi in enumerate(x):
    for j, yj in enumerate(y):
        r1 = np.sqrt((xi - distance/2)**2 + yj**2)  # Distance to charge 1
        r2 = np.sqrt((xi + distance/2)**2 + yj**2)  # Distance to charge 2
        potential[i, j] = charge_1 / (4 * np.pi * epsilon_0 * r1) + charge_2 / (4 * np.pi * epsilon_0 * r2)

# Calculate the partial derivatives of the potential
dVdx, dVdy = np.gradient(potential, x, y)

# Calculate the electric field components Ex and Ey
Ex = -dVdx
Ey = -dVdy

# Calculate the magnitude and direction of the electric field
magnitude = np.sqrt(Ex**2 + Ey**2)
direction = np.arctan2(Ey, Ex)

# Create a density plot of the magnitude of the electric field
plt.imshow(magnitude.T, extent=(-0.5, 0.5, -0.5, 0.5), origin='lower', cmap='hot')
plt.colorbar(label='Electric Field Magnitude (V/m)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric Field Magnitude')
plt.show()

# Create a density plot of the direction of the electric field
plt.imshow(direction.T, extent=(-0.5, 0.5, -0.5, 0.5), origin='lower', cmap='hsv')
plt.colorbar(label='Electric Field Direction (radians)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric Field Direction')
plt.show()

# Create a density plot of the potential
plt.imshow(potential.T, extent=(-0.5, 0.5, -0.5, 0.5), origin='lower', cmap='hot')
plt.colorbar(label='Electric Potential (V)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric Potential')
plt.show()