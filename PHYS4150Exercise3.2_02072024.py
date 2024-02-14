import numpy as np 
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi)
x = 2*np.cos(theta) + np.cos(2*(theta))
y = 2*np.sin(theta) + np.sin(2*(theta))

plt.plot(x,y)
plt.show()

theta = np.linspace(0,10*np.pi)
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y)
plt.show()

theta = np.linspace(0,24*np.pi)
r = np.exp(np.cos(theta)) - 2*np.cos(4*(theta)) + (np.sin((theta)/12))**5
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y)
plt.show()

