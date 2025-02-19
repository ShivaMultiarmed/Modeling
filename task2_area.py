import numpy as np
import matplotlib.pyplot as plt
import random

S = 2 - np.sqrt(2)

def density(x):
    if x < np.pi / 4:
        return np.sin(x)
    else:
        return np.cos(x)

def create_x(ksi):
    if ksi < 0.5:
        x = np.arccos(1 - S * ksi)
    else:
        x = np.arcsin(S * ksi + np.sqrt(2) - 1)
    return x

x_values = []
y_values = []

for i in range(0, 1000):
    ksi1 = random.random()
    ksi2 = random.random()
    x = create_x(ksi1)
    x_values.append(x)
    y_values.append(ksi2 * density(x))

# graph_x = [x for x in np.arange(0, np.pi / 2, 0.001)]
# graph_y = [density(x) for x in graph_x]

plt.scatter(x_values, y_values, s = 5, c = "#506c96")
# plt.scatter(graph_x, graph_y, s = 5, c = "#9c6b46")
# plt.scatter(graph_x, [0 for x in graph_x], s = 5, c = "#9c6b46")

plt.show()