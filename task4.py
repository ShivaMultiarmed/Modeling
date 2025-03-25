from random import random
import matplotlib.pyplot as plt

states_num = 10

matrix = [[ random() for j in range(0, states_num)] for i in range(0, states_num)]
for i in range(0, states_num):
    print()
    sum_in_row = sum(matrix[i])
    for j in range(0, states_num):
        matrix[i][j] = matrix[i][j] / sum_in_row
        print(str("{:.3f}").format(matrix[i][j]) + "\t", end="")
    sum_in_row = sum(matrix[i])
    print("\t | {:.3f}".format(sum_in_row))

print("==================== Суммы по столбцам =====================")

for i in range(states_num):
    column = [matrix[j][i] for j in range(states_num)]
    print("{:.3f} \t".format(sum(column)), end="")


state_counts = [0 for i in range(0,states_num)]
current_state = int(random() * states_num)

for i in range(0, 1000):
    ksi = random()
    new_state = states_num - 1
    for j in range(0, states_num):
        if ksi < sum(matrix[current_state][0:j + 1]):
            new_state = j
            break
    current_state = new_state
    state_counts[current_state] += 1

print()
print("==================== Количество переходов в каждое состояние =====================")
for state_count in state_counts:
    print(f"{state_count}\t\t", end="")
print("\t| " + str(sum(state_counts)))

plt.bar(range(1, states_num + 1), state_counts, alpha=0.6, color='b', edgecolor='black')
plt.xlabel("Номера состояний")
plt.ylabel("Количество переходов")
plt.show()