import matplotlib.pyplot as plt 
import random as rand  
import math

def getp1(d, a, b):
    return math.pow(math.e, -a * math.pow(d, b))

def getp2(d, b): 
    return 1 / (math.pow(d, b))

MAX = 9999              # max value 
total = 50              # total vertex (points) number
count = total           # counter for vertex
grid = 100              # grid side length
max_dist = 20           # max distance between points
min_dist = 2            # max distance between points
max_deg = 5             # max vertex degree
a = 2.0 
b = 2.0 
x1 = []                 # array of used vertices
deg = [0] * total       # array of degree of used vertices
dist = []               # temp distance of available vertices
num = []                # numbers of available vertices
x = []                  # x coord of vertex 
y = []                  # y coord of vertex

print(f'Размер области: {grid}x{grid}')
print(f'Количество узлов: {total}')
print(f'Мин. расстояние между узлами: {min_dist}')
print(f'Макс. расстояние между узлами: {max_dist}')
print(f'Макс. степень вершины: {max_deg}')
print(f'Зависимость вероятности выбора\nребра от расстояния d:\ne ^ (-a * d ^ b), a = {a}, b = {b}')

same_points = False      # if same_points True, points - same, graph - random 
if same_points: 
    rand.seed(1000)

fig, ax = plt.subplots(figsize=(5, 5)) 
ax.grid(True)
x.append(int(rand.uniform(0, grid))) 
y.append(int(rand.uniform(0, grid))) 
count -= 1 
# create vertices (points)

while count != 0: 
    tx1 = 0 
    ty1 = 0 
    flag = True 
    while flag: 
        tx = int(rand.uniform(min_dist, max_dist)) 
        ty = int(rand.uniform(min_dist, max_dist)) 
        rx = rand.random() 
        ry = rand.random() 
        tlen = len(x) - 1 
        cond = 0
        if rx < 0.5:
            tx1 = x[tlen] - tx 
        else:
            tx1 = x[tlen] + tx 
        if ry < 0.5:
            ty1 = y[tlen] - ty
        else: 
            ty1 = y[tlen] + ty 
        cond = math.sqrt((tx1 - x[tlen]) * (tx1 - x[tlen]) + (ty1 - y[tlen]) * (ty1 - y[tlen]))
        if tx1 < 0 or tx1 > grid or ty1 < 0 or ty1 > grid or cond > max_dist: 
            continue

        flag = False

        for j in range(0, tlen): 
            cond = math.sqrt((tx1 - x[j]) ** 2 + (ty1 - y[j]) ** 2)

            if cond < min_dist: 
                flag = True 
                break
    rr = rand.random() 
    x.append(tx1) 
    y.append(ty1) 
    count -= 1

# fill adjacency matrix with MAX
arr = [[MAX for _ in range(total)] for _ in range(total)]

# fill adjacency matrix with MAX for final graph
arrf = [[MAX for _ in range(total)] for _ in range(total)]

# create adjacency matrix 
for i in range(total): 
    for j in range(i + 1, total): 
        temp = math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) 
        if temp <= max_dist: 
            arr[i][j] = float('{:.3f}'.format(temp)) 
            arr[j][i] = float('{:.3f}'.format(temp))

# save matrix 
sourceFile = open('demo.txt', 'w') 
stringified_matrix = '\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in arr])
print(stringified_matrix, file = sourceFile)
sourceFile.close()

if same_points: 
    rand.seed()

# create graph 
count = total 
root = int(rand.uniform(0, total))  # set root
print("Начальная вершина:", root)
x1.append(root) 
deg[root] = 1 
t_sum = 0 
while count != 0:
    if count == total:
        for i in range(total): 
            if arr[root][i] <= MAX:
                cur_sum = getp1(arr[root][i], a, b) 
                t_sum += cur_sum 
                dist.append(cur_sum) 
                num.append(i) 
        for i in range(len(dist)): 
            dist[i] /= t_sum 
        t_sum = 0 
        rn = rand.random()
        cs = 0 
        for i in range(len(dist)): 
            if cs + dist[i] < rn: 
                cs += dist[i] 
            else: 
                x1.append(num[i]) 
                deg[num[i]] += 1 
                arrf[root][num[i]] = arr[root][num[i]] 
                arrf[num[i]][root] = arr[num[i]][root] 
                xi = [x[root], x[num[i]]] 
                yi = [y[root], y[num[i]]] 
                ax.plot(xi, yi, '#2f6ead', linewidth=1)
                dist.clear() 
                num.clear() 
                break 
    else: 
        for j in range(len(x1)): 
            dist.append([]) 
            num.append([]) 
            for i in range(total): 
                if arr[x1[j]][i] != MAX and deg[x1[j]] < max_deg and deg[i] == 0: 
                    cur_sum = getp1(arr[x1[j]][i], a, b) 
                    t_sum += cur_sum
                    dist[j].append(cur_sum) 
                    num[j].append(i) 
        for j in range(len(x1)): 
            for i in range(len(dist[j])): 
                dist[j][i] /= t_sum 
        t_sum = 0 
        rn = rand.random() 
        cs = 0 
        qwe = False 
        for j in range(len(x1)): 
            if qwe: 
                break 
            for i in range(len(dist[j])): 
                if cs + dist[j][i] < rn: 
                    cs += dist[j][i] 
                else: 
                    arrf[x1[j]][num[j][i]] = arr[x1[j]][num[j][i]] 
                    arrf[num[j][i]][x1[j]] = arr[num[j][i]][x1[j]] 
                    x1.append(num[j][i]) 
                    deg[num[j][i]] += 1 
                    deg[x1[j]] += 1 
                    xi = [x[x1[j]], x[num[j][i]]] 
                    yi = [y[x1[j]], y[num[j][i]]] 
                    ax.plot(xi, yi, '#2f6ead', linewidth=1)
                    dist.clear() 
                    num.clear() 
                    qwe = True 
                    break 
    count -= 1 
 
# save matrix 
sourceFile1 = open('demo1.txt', 'w') 
stringified_matrix = '\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in arrf])
print(stringified_matrix, file = sourceFile1)
sourceFile1.close()

# calc min dist 
vec = [0] * total 
for k in range(total): 
    for i in range(total): 
        for j in range(total): 
            if i != j: 
                arrf[i][j] = min(arrf[i][j], arrf[i][k]+arrf[k][j]) 
sourceFile2 = open('demo2.txt', 'w')
stringified_matrix = '\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in arrf])
print(stringified_matrix, file = sourceFile2)
sourceFile2.close()

# calc max of mins (diametr) 
max = 0 
for i in range(total): 
    for j in range(i + 1, total): 
        if arrf[i][j] > max and arrf[i][j] != MAX: 
            max = arrf[i][j] 
#print("Diametr: ", max)

# print points  
point = 0 
if point == 1: 
    for i in range(len(x)): 
        print("(" + str(x[i]) + ", " + str(y[i]) + ")", end = "; ") 
ax.plot(x , y, 'o', color = '#ad722f', markersize=5)
ax.plot(x[root], y[root], 'o', color = '#2f6ead')
# print point num
text = 0 
if text == 1: 
    for i in range(len(x)): 
        ax.text(x[i], y[i], str(i), size=10) 
    ax.axis('equal')

ax.set_xlim([0 - 2, grid + 2]) 
ax.set_ylim([0 - 2, grid + 2]) 
plt.show()