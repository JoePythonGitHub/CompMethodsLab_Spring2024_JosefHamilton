import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1  # mass of cannonball (kg)
g = 9.81  # acceleration due to gravity (m/s^2)
rho = 1.22  # density of air (kg/m^3)
C = 0.47  # coefficient of drag for a sphere
R = 0.08  # radius of cannonball (m)
A = np.pi * R**2  # cross-sectional area of cannonball (m^2)

# Initial conditions
v0 = 100  # initial velocity (m/s)
theta = 30  # angle of launch (degrees)
x0, y0 = 0, 0  # initial position (m)

# Convert angle to radians
theta = np.radians(theta)

# Define equations of motion

def f(r, t):
    vx, vy, x, y = r
    v = np.sqrt(vx**2 + vy**2)
    dxdt = vx
    dydt = vy
    dvxdt = -(0.5*rho*C*A*v*vx) / m
    dvydt = -g - (0.5*rho*C*A*v*vy) / m
    return np.array([dvxdt, dvydt, dxdt, dydt], float)

# Time interval and step size
t0, tf = 0, 20
h = 0.1

# Create arrays for t and r values
t_points = np.arange(t0, tf, h)
x_points = []
y_points = []



# Solve equations of motion using the fourth-order Runge-Kutta method
r = np.array([v0*np.cos(theta), v0*np.sin(theta), x0, y0], float)
for t in t_points:
    x_points.append(r[2])
    y_points.append(r[3])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5*k1, t + 0.5*h)
    k3 = h * f(r + 0.5*k2, t + 0.5*h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2*k2 + 2*k3 + k4) / 6



# Plot trajectory
plt.plot(x_points, y_points)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Cannonball Trajectory')
plt.show()



