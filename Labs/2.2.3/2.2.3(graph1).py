import numpy as np
import matplotlib.pyplot as plt


X_1 = [97.15, 92.26, 86.82, 80.64, 73.56, 65.10, 54.47, 18.5, 5.99, 1.905]
Y_1 = [2.05, 1.94, 1.82, 1.68, 1.52, 1.34, 1.11, 0.372, 0.12, 0.0382]
t_1 = 1.05 * max(X_1)
model_1 = np.polyfit(X_1, Y_1, 1)
x_1 = [0, t_1]
y_1 = [model_1[1], (model_1[0] * t_1 + model_1[1])]


X_2 = [95.82, 91.06, 85.75, 79.71, 72.78, 64.47, 54.03, 18.45, 5.98, 1.904]
Y_2 = [2.07, 1.96, 1.84, 1.7, 1.54, 1.36, 1.13, 0.381, 0.123, 0.0393]
model_2 = np.polyfit(X_2, Y_2, 1)
t_2 = 1.05 * max(X_2)
x_2 = [0, t_2]
y_2 = [model_2[1], (model_2[0] * t_2 + model_2[1])]


X_3 = [94.21, 89.59, 84.45, 78.57, 71.82, 63.72, 53.50, 18.39, 5.97, 1.903]
Y_3 = [2.10, 1.99, 1.87, 1.73, 1.57, 1.39, 1.16, 0.393, 0.128, 0.04064]
model_3 = np.polyfit(X_3, Y_3, 1)
t_3 = 1.05 * max(X_3)
x_3 = [0, t_3]
y_3 = [model_3[1], (model_3[0] * t_3 + model_3[1])]


X_4 = [1.903, 5.97, 18.32, 52.97, 62.99, 70.90, 77.47, 83.19, 88.18, 92.67]
Y_4 = [0.042, 0.132, 0.405, 1.18, 1.42, 1.60, 1.76, 1.9, 2.02, 2.13]
model_4 = np.polyfit(X_4, Y_4, 1)
t_4 = 1.05 * max(X_4)
x_4 = [0, t_4]
y_4 = [model_4[1], (model_4[0] * t_4 + model_4[1])]


X_5 = [91.17, 86.82, 81.96, 76.40, 69.99, 62.26, 52.47, 18.26, 5.961, 1.9]
Y_5 = [2.16, 2.05, 1.93, 1.79, 1.63, 1.44, 1.21, 0.416, 0.136, 0.04332]
model_5 = np.polyfit(X_5, Y_5, 1)
t_5 = 1.05 * max(X_5)
x_5 = [0, t_5]
y_5 = [model_5[1], (model_5[0] * t_5 + model_5[1])]



X_6 = [1.901, 5.95, 18.2, 51.96, 61.56, 69.12, 75.36, 80.76, 85.48, 89.7]
Y_6 = [0.0447, 0.140, 0.428, 1.24, 1.47, 1.66, 1.82, 1.96, 2.08, 2.19]
model_6 = np.polyfit(X_6, Y_6, 1)
t_6 = 1.05 * max(X_6)
x_6 = [0, t_6]
y_6 = [model_6[1], (model_6[0] * t_6 + model_6[1])]


X_7 = [87.6, 83.56, 79.03, 73.81, 67.8, 60.50, 51.2, 18.1, 5.945, 1.90]
Y_7 = [2.23, 2.12, 2.0, 1.85, 1.70, 1.51, 1.27, 0.445, 0.146, 0.0467]
model_7 = np.polyfit(X_7, Y_7, 1)
t_7 = 1.05 * max(X_7)
x_7 = [0, t_7]
y_7 = [model_7[1], (model_7[0] * t_7 + model_7[1])]



print(model_1)
print(model_2)
print(model_3)
print(model_4)
print(model_5)
print(model_6)
print(model_7)


plt.figure(figsize=(10, 5))
plt.scatter(X_1, Y_1)
plt.plot(x_1, y_1, label=r'$T_1=22 \degree C$')
plt.scatter(X_2, Y_2)
plt.plot(x_2, y_2, label=r'$T_2=30 \degree C$')
plt.scatter(X_3, Y_3)
plt.plot(x_3, y_3, label=r'$T_3=40 \degree C$')
plt.scatter(X_4, Y_4)
plt.plot(x_4, y_4, label=r'$T_4=50 \degree C$')
plt.scatter(X_5, Y_5)
plt.plot(x_5, y_5, label=r'$T_5=60 \degree C$')
plt.scatter(X_6, Y_6)
plt.plot(x_6, y_6, label=r'$T_6=70 \degree C$')
plt.scatter(X_7, Y_7)
plt.plot(x_7, y_7, label=r'$T_7=85 \degree C$')
plt.xlabel(r'$I, mA$', fontsize=14)
plt.ylabel(r'$U, V$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()
