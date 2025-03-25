from random import random

states_num = 10
iterations = 20

matrix = [[ random() for j in range(0, states_num)] for i in range(0, states_num)]

for m in range(iterations):
    print(f"\nИтерация № {m}")
    for i in range(states_num):
        print()
        sum_in_row = sum(matrix[i])
        for j in range(states_num):
            matrix[i][j] = matrix[i][j] / sum_in_row
            print(str("{:.3f}").format(matrix[i][j]) + "\t", end="")
        sum_in_row = sum(matrix[i])
        print("\t | {:.3f}".format(sum_in_row))
    print()
    print("==================== Суммы по столбцам =====================")


    for i in range(states_num):
        column = [matrix[j][i] for j in range(states_num)]
        print("{:.3f} \t".format(sum(column)), end="")
    print("\n")
    for i in range(0, states_num):
        print()
        for j in range(states_num):
            col = [matrix[n][j] for n in range(states_num)]
            sum_in_col = sum(col)
            matrix[i][j] = matrix[i][j] / sum_in_col
            print(str("{:.3f}").format(matrix[i][j]) + "\t", end="")
        col = [matrix[n][i] for n in range(states_num)]
        sum_in_col = sum(col)
        print("\t | {:.3f}".format(sum_in_col))
    print("==================== Суммы по столбцам =====================")

    for i in range(states_num):
        column = [matrix[j][i] for j in range(states_num)]
        print("{:.3f} \t".format(sum(column)), end="")

    print("\n")