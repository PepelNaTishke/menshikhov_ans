import sys
from collections import deque

def input_data():
    global n, mas, start, end
    data = sys.stdin.read().split('\n')
    n = int(data[0])
    mas = []
    for i in range(n):
        row = list(data[i + 1])
        mas.append(row)
        for j in range(n):
            if row[j] == '@':
                start = (i, j)
            if row[j] == 'X':
                end = (i, j)

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

def correct(x, y):
    return 0 <= x < n and 0 <= y < n

def find_way():
    global f
    f = [[0] * n for _ in range(n)]
    f[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for i in range(4):
            x = cur[0] + move_x[i]
            y = cur[1] + move_y[i]
            if correct(x, y) and f[x][y] == 0 and mas[x][y] != 'O':
                f[x][y] = f[cur[0]][cur[1]] + 1
                if (x, y) == end:
                    return
                q.append((x, y))

def find_answer():
    cur = end
    value = f[end[0]][end[1]] - 1
    mas[end[0]][end[1]] = '+'
    while cur != start:
        for i in range(4):
            x = cur[0] + move_x[i]
            y = cur[1] + move_y[i]
            if correct(x, y) and f[x][y] == value:
                value -= 1
                if value != 0:
                    mas[x][y] = '+'
                cur = (x, y)
                break

def output():
    for row in mas:
        print(''.join(row))

def solve():
    find_way()
    if not f[end[0]][end[1]]:
        print("N")
    else:
        print("Y")
        find_answer()
        output()

input_data()
solve()