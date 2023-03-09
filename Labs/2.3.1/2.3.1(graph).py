import numpy as np
import matplotlib.pyplot as plt

t = [0, 5, 10, 16, 21, 26, 32, 40, 47, 52, 57, 66, 74]
ln = [9 * 10**(-5), 1.2 * 10**(-4), 1.6 * 10**(-4),
      2.0 * 10**(-4), 2.4 * 10**(-4), 2.8 * 10**(-4), 3.2 * 10**(-4), 3.8 * 10**(-4), 4.2 * 10**(-4), 4.6 * 10**(-4), 5.0 * 10**(-4), 5.5 * 10**(-4), 6.0 * 10**(-4)]

model = np.polyfit(t, ln, 1)
x = [0, 80]
y = [model[1], (model[0] * 80 + model[1])]

print(model)

plt.figure(figsize=(10, 5))
plt.scatter(t, ln)
plt.plot(x, y, color='r')
plt.xlabel(r'$t, c$', fontsize=14)
plt.ylabel(r'$P$', fontsize=14)
plt.grid(True)
plt.show()
