import numpy as np
import matplotlib.pyplot as plt
import math


X = np.array([1, 2, 3, 4, 5, 6, 7, 11, 12, 20, 30, 40, 50, 100])
Y = np.array([6735, 5340, 4163, 3403, 2925, 2513, 2098, 1554, 1399, 632, 305, 150, 43, 5])

plt.figure(figsize=(10, 5))
plt.scatter(X, Y)
plt.xlabel(r'Количество частиц', fontsize=14)
plt.ylabel(r'Среднее число ходов', fontsize=14)
plt.show()
