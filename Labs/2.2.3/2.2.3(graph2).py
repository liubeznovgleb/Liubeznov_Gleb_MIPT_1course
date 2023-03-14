import numpy as np
import matplotlib.pyplot as plt

X = [95.82, 91.06, 85.75, 79.71, 72.78, 64.47, 54.03, 18.45, 5.98, 1.904]

Y = [2.07, 1.96, 1.84, 1.7, 1.54, 1.36, 1.13, 0.381, 0.123, 0.0393]

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
