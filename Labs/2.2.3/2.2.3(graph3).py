import numpy as np
import matplotlib.pyplot as plt

X = [94.21, 89.59, 84.45, 78.57, 71.82, 63.72, 53.50, 18.39, 5.97, 1.903]

Y = [2.10, 1.99, 1.87, 1.73, 1.57, 1.39, 1.16, 0.393, 0.128, 0.04064]

t = 1.05 * max(X)

model = np.polyfit(X, Y, 1)
x = [0, t]
y = [model[1], (model[0] * t + model[1])]

print(model)

plt.figure(figsize=(10, 5))
plt.scatter(X, Y)
plt.plot(x, y, color='r')
plt.xlabel(r'$I, mA$', fontsize=14)
plt.ylabel(r'$U, V$', fontsize=14)
plt.grid(True)
plt.show()
