from collections.abc import Callable
from random import random
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt


def generate_matrix(states_num: int) -> list[list[float]]:
    matrix = [[random() for j in range(0, states_num)] for i in range(0, states_num)]

    iterations = 20

    for m in range(iterations):
        for i in range(states_num):
            sum_in_row = sum(matrix[i])
            for j in range(states_num):
                matrix[i][j] = matrix[i][j] / sum_in_row

        for i in range(0, states_num):
            for j in range(states_num):
                col = [matrix[n][j] for n in range(states_num)]
                sum_in_col = sum(col)
                matrix[i][j] = matrix[i][j] / sum_in_col
    return matrix

def print_matrix(matrix: list[list[float]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str("{:.3f}").format(matrix[i][j]) + "\t", end="")
        sum_in_row = sum(matrix[i])
        print("\t | {:.3f}".format(sum_in_row))
    print()
    print("==================== Суммы по столбцам =====================")

    for i in range(len(matrix[0])):
        column = [matrix[j][i] for j in range(len(matrix))]
        print("{:.3f} \t".format(sum(column)), end="")
    print("\n")

def generate_random() -> float:
    ksi = random()
    k = -0.76178
    if ksi < 0.144:
        x = 0.2 * (1500 * ksi) ** (1 / 3) - 0.2
    else:
        x = 2.5 - np.sqrt(2.25 + (2 / k) * (ksi - 0.144))

    x_min = -0.2
    x_max = 2.5

    return (x - x_min) / (x_max - x_min)

def play_process(
        matrix: list[list[float]],
        f: Callable[[], float]
) -> Tuple[list[int], list[int]]:
    states_num = len(matrix)
    states = []
    state_counts = [0 for _ in range(states_num)]
    current_state = int(random() * states_num)
    for i in range(100_000):
        ksi = f()
        new_state = 0
        for j in range(states_num):
            if ksi < sum(matrix[current_state][0:j + 1]):
                new_state = j
                break
        current_state = new_state
        states.append(current_state)
        state_counts[current_state] += 1

    return states, state_counts

def show_histogram(data: list[int]) -> None:
    plt.bar(range(1, len(data) + 1), data, alpha=0.6, color='b', edgecolor='black')
    plt.xlabel("Номера состояний")
    plt.ylabel("Количество переходов")
    plt.show()


def evaluate_auto_correlation(data: list[int]) -> list[float]:
    data = np.asarray(data, dtype=float)
    N = len(data)
    avg = np.mean(data)
    centered = data - avg
    var = np.sum(centered ** 2)
    return [np.sum(centered[:N-k] * centered[k:]) / var for k in range(N)]

def show_auto_correlation(data: list[float]):
    plt.stem(range(1, len(data) + 1), data) #, use_line_collection=True)
    plt.xlabel('Лаг')
    plt.ylabel('Автокорреляция')
    plt.title('Автокорреляционная функция')
    plt.grid(True)
    plt.show()

states_num = 50
matrix_a = generate_matrix(states_num)
matrix_b = generate_matrix(states_num)
print_matrix(matrix_a)
print_matrix(matrix_b)
process_a, process_a_count = play_process(matrix_a, generate_random)
process_b, process_b_count = play_process(matrix_b, generate_random)
print(process_a)
print(process_b)
show_histogram(process_a_count)
show_histogram(process_b_count)
auto_correlation_a = evaluate_auto_correlation(process_a)
auto_correlation_b = evaluate_auto_correlation(process_b)
show_auto_correlation(auto_correlation_a[0:10])
show_auto_correlation(auto_correlation_b[0:10])