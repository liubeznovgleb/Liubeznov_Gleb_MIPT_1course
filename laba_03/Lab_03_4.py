import numpy as np
import matplotlib.pyplot as plt
import math


X = np.array([16, 18, 18, 18, 17, 16, 14, 11, 10, 8, 6, 6])
Y = np.arange(2, len(X) + 2, 1)

plt.figure(figsize=(10, 5))
plt.scatter(Y, X)
plt.xlabel(r'Количество частиц', fontsize=14)
plt.ylabel(r'Среднее число ходов', fontsize=14)
plt.show()
