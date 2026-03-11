import sys
from collections import deque

KNIGHT = '@'

move_x = [-2,-2,-1,-1, 1, 1, 2, 2]
move_y = [-1, 1,-2, 2,-2, 2,-1, 1]

data = sys.stdin.read().split()
n = int(data[0])
field = [list(data[i + 1]) for i in range(n)]

knights = [(i, j) for i in range(n) for j in range(n) if field[i][j] == KNIGHT]
start, end = knights[0], knights[1]

mas = [[0] * n for _ in range(n)]

def correct(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    mas[start[0]][start[1]] = 1
    q = deque([start])
    while q:
        cx, cy = q.popleft()
        for i in range(8):
            x, y = cx + move_x[i], cy + move_y[i]
            if correct(x, y) and field[x][y] != '#' and mas[x][y] == 0:
                mas[x][y] = mas[cx][cy] + 1
                q.append((x, y))
                if (x, y) == end:
                    return

def find_answer():
    cur = end
    while cur != start:
        cx, cy = cur
        for i in range(8):
            x, y = cx + move_x[i], cy + move_y[i]
            if correct(x, y) and mas[x][y] + 1 == mas[cx][cy]:
                cur = (x, y)
                field[x][y] = KNIGHT
                break

bfs()

if mas[end[0]][end[1]] != 0:
    find_answer()
    for row in field:
        print(''.join(row))
else:
    print("Impossible")