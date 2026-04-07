import sys
from sys import setrecursionlimit

setrecursionlimit(10000)

MAX_SIZE = 36
mas = [[''] * MAX_SIZE for _ in range(MAX_SIZE)]

def input_data():
    global n, mas
    data = sys.stdin.read().split('\n')
    n = int(data[0])
    for i in range(1, n + 1):
        row = data[i]
        for j in range(1, n + 1):
            mas[i][j] = row[j - 1]
    for i in range(n + 2):
        mas[0][i] = '#'
        mas[n + 1][i] = '#'
        mas[i][0] = '#'
        mas[i][n + 1] = '#'

moveX = [0, 1, 0, -1]
moveY = [1, 0, -1, 0]

def DFS(x, y, walls):
    if mas[x][y] == '.':
        mas[x][y] = 'X'
    else:
        return walls
    for i in range(4):
        nx, ny = x + moveX[i], y + moveY[i]
        if mas[nx][ny] == '#':
            walls += 1
    for i in range(4):
        nx, ny = x + moveX[i], y + moveY[i]
        if mas[nx][ny] == '.':
            walls = DFS(nx, ny, walls)
    return walls

def solve():
    walls = 0
    walls = DFS(1, 1, walls)
    walls = DFS(n, n, walls)
    print((walls - 4) * 9)

def main():
    input_data()
    solve()

main()
