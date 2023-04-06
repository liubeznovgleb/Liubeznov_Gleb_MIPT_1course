import numpy as np
import matplotlib.pyplot as plt
import math


X = np.array([1, 2, 3, 4, 5, 6, 7, 11, 12, 20, 30, 40, 50, 100])
Y = np.array([25, 33, 36, 38, 41, 43, 44, 42, 40, 22, 10, 6, 4])

plt.figure(figsize=(10, 5))
plt.scatter(X, Y)
plt.xlabel(r'Размер поля n * n', fontsize=14)
plt.ylabel(r'Среднее число ходов', fontsize=14)
plt.show()
