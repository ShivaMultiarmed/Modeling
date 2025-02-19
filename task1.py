import numpy as np
import random
import matplotlib.pyplot as plt

k = -0.76178

def quantile(ksi):
    if ksi < 0.144:
        return 0.2 * (1500 * ksi) ** (1/3) - 0.2
    else:
        return 2.5 - np.sqrt(2.25 + (2/k) * (ksi - 0.144))

def random_sensor():
    ksi = random.random()
    return quantile(ksi)

samples = [random_sensor() for _ in range(1000000)]

plt.hist(samples, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
plt.xlabel('x')
plt.ylabel('Плотность')
plt.grid(True)
plt.show()