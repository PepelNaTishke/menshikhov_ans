import sys
from collections import deque

def input_data():
    global n, m, mas
    data = sys.stdin.read().split('\n')
    n, m = map(int, data[0].split())
    mas = [list(data[i + 1]) for i in range(n)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

def correct(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + move_x[i], cy + move_y[i]
            if correct(nx, ny) and mas[nx][ny] == '#':
                mas[nx][ny] = '.'
                q.append((nx, ny))

def solve():
    amount = 0
    for i in range(n):
        for j in range(m):
            if mas[i][j] == '#':
                mas[i][j] = '.'
                bfs(i, j)
                amount += 1
    print(amount)

input_data()
solve()