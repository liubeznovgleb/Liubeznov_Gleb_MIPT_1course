import numpy as np
import matplotlib.pyplot as plt

L = [1 / 40, 1 / 86, 1 / 173, 1 / 188]

D = [0.63555 / 276.1190,0.503085 / 373.347,
     0.307308 / 440.002, 0.385336 / 556.09]


D_1 = [5000 * 0.63555 / 276.1190, 5000 * 0.503085 / 373.347,
     5000 * 0.307308 / 440.002, 5000 * 0.385336 / 556.09]

model = np.polyfit(L, D, 1)
x = [0, 1 / 35]
y = [5000 * model[1], 5000 * (model[0] / 35 + model[1])]

print(x, y)

plt.figure(figsize=(10, 5))
plt.scatter(L, D_1)
plt.plot(x, y, color='r')
plt.xlabel(r'$\frac{1}{P}, \frac{1}{торр}$', fontsize=14)
plt.ylabel(r'$D, \frac{см^2}{c}$', fontsize=14)
plt.grid(True)
plt.savefig('2.1.1(2).png')
plt.show()

