import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set lattice size
L = 101

# Initialize particle position at the center of the lattice
i, j = L // 2, L // 2

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(0, L)

# Initialize scatter plot for particle position
scat = ax.scatter(i, j, c='r', marker='o')

# Define function to update particle position
def update(frame):
    global i, j
    # Choose a random direction (up, down, left, or right)
    direction = np.random.choice(['up', 'down', 'left', 'right'])
    # Update particle position based on chosen direction
    if direction == 'up':
        i = max(0, i - 1)
    elif direction == 'down':
        i = min(L - 1, i + 1)
    elif direction == 'left':
        j = max(0, j - 1)
    elif direction == 'right':
        j = min(L - 1, j + 1)
    # Update scatter plot data
    scat.set_offsets((i, j))
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=10, blit=True)

# Show the animation
plt.show()
