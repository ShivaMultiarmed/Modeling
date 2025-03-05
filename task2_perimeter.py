from random import random

import numpy as np

import matplotlib.pyplot as plt

def density(x):
    if x < np.pi / 4:
        return np.sin(x)
    else:
        return np.cos(x)

S = 2 - np.sqrt(2)

def evaluate_perimeter(function, step, start, end):
    P = 0
    for x in np.arange(start, end, step):
        height = function(x + step) - function(x)
        part = np.sqrt(np.square(height) + np.square(step))
        P += part
    return P

perimeter_1 = evaluate_perimeter(np.sin, 0.00001, 0, np.pi / 4) # длина дуги для sin
perimeter_2 = evaluate_perimeter(np.cos, 0.00001, np.pi / 4, np.pi / 2) # длина дуги для cos
perimeter_3 = np.pi / 2 # прямая на оси x
perimeter = perimeter_1 + perimeter_2 + perimeter_3
print(str(perimeter))

def create_point_on_graph():
    ksi = random()
    ksi2 = random()
    if ksi < perimeter_1 / perimeter:
        x = ksi2 * np.pi / 4
        y = np.sin(x)
    elif ksi < (perimeter_1 + perimeter_2) / perimeter:
        x = ksi2 * np.pi / 4 + np.pi / 4
        y = np.cos(x)
    else:
        x = ksi2 * np.pi / 2
        y = 0
    return x, y

points = [create_point_on_graph() for i in range(0, 1000)]
x_values, y_values = zip(*points)
plt.scatter(x_values, y_values, s = 5, c = "#506c96")
plt.show()