import numpy as np
import matplotlib.pyplot as plt


X_1 = [17023, 2 * 12589, 3 * 15527, 4 * 22572, 5 * 19023,
       6 * 17778, 7 * 15239, 8 * 18908, 9 * 19621, 10 * 6376]
Y_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t_1 = 1.05 * max(X_1)
model_1 = np.polyfit(X_1, Y_1, 1)
x_1 = [0, t_1]
y_1 = [model_1[1], (model_1[0] * t_1 + model_1[1])]


print(model_1)


plt.figure(figsize=(10, 5))
plt.scatter(X_1, Y_1)
plt.plot(x_1, y_1, label=r'$T_1=22 \degree C$')
plt.xlabel(r'$I, mA$', fontsize=14)
plt.ylabel(r'$U, V$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()
