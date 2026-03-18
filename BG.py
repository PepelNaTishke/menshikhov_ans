from collections import deque

n = int(input())
grid = []
start = None

for z in range(n):
    input()
    layer = []
    for x in range(n):
        row = input()
        layer.append([1 if ch == '#' else 0 for ch in row])
        if 'S' in row:
            start = (z, x, row.index('S'))
    grid.append(layer)

dx = [0, 0,  0, 0, -1, 1]
dy = [0, 0, -1, 1,  0, 0]
dz = [-1, 1, 0, 0,  0, 0]

def ok(z, x, y):
    return 0 <= z < n and 0 <= x < n and 0 <= y < n

def bfs():
    init = 2
    sz, sx, sy = start
    grid[sz][sx][sy] = init
    q = deque([(sz, sx, sy)])

    while q:
        cz, cx, cy = q.popleft()
        if cz == 0:
            print(grid[cz][cx][cy] - init)
            return
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            if ok(nz, nx, ny) and grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = grid[cz][cx][cy] + 1
                q.append((nz, nx, ny))

bfs()
