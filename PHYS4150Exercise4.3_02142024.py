import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0
def func(x):
    ans = x*(x-1)
    return ans

delta = 10.**(np.arange(-14, -2))

df = (func(x+delta-func(x)))/delta
print (df)

plt.plot(delta, df)
plt.show()