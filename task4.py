from random import random
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

states_num = 10

matrix = [[ random() for j in range(0, states_num)] for i in range(0, states_num)]
for i in range(0, states_num):
    sum_in_row = sum(matrix[i])
    for j in range(0, states_num):
        matrix[i][j] = matrix[i][j] / sum_in_row

print(matrix)

state_counts = [0 for i in range(0,states_num)]
current_state = int(random() * states_num)

for i in range(0, 1000):
    ksi = random()
    for j in range(0, states_num):
        if ksi < sum(matrix[current_state][0:j + 1]):
            current_state = j
            break
    state_counts[current_state] += 1

plt.grid(linestyle="--")
plt.scatter(range(1, states_num + 1), state_counts)
plt.xlabel("Номера состояний")
plt.ylabel("Количество переходов")
plt.xticks(range(0, states_num + 2))
plt.show()