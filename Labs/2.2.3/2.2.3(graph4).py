import numpy as np
import matplotlib.pyplot as plt

X = [1.903, 5.97, 18.32, 52.97, 62.99, 70.90, 77.47, 83.19, 88.18, 92.67]

Y = [0.042, 0.132, 0.405, 1.18, 1.42, 1.60, 1.76, 1.9, 2.02, 2.13]

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
