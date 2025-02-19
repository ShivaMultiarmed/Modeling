import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.colorizer import Colorizer

S = 2 - np.sqrt(2)

def density(x):
    if x < np.pi / 4:
        return np.sin(x)
    else:
        return np.cos(x)

def create_point(ksi1, ksi2):
    if ksi1 < 0.5:
        x = np.arccos(1 - S * ksi1)
    else:
        x = np.arcsin(S * ksi1 + np.sqrt(2) - 1)
    y = ksi2 * density(x)
    return x, y

x_values = []
y_values = []

for i in range(0, 1000):
    ksi1 = random.random()
    ksi2 = random.random()
    x, y = create_point(ksi1, ksi2)
    x_values.append(x)
    y_values.append(y)

graph_x = [x for x in np.arange(0, np.pi / 2, 0.001)]
graph_y = [density(x) for x in graph_x]

plt.scatter(x_values, y_values, s = 10, c = "#235416")
plt.scatter(graph_x, graph_y, s = 10, c = "#453412")
plt.scatter(graph_x, [0 for x in graph_x], s = 10, c = "#453412")

plt.show()