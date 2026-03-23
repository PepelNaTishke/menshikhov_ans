MARKED = -(1000 * 1000 * 1000)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
grid  = [[0] * n for _ in range(n)]
waves = [[0] * n for _ in range(n)]

starts = []
queue  = []
num = 1

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        grid[i][j] = row[j]
        if row[j] != 0:
            starts.append((i, j))
            queue.append([i, j, num])
            num += 1

def ok(x, y):
    return 0 <= x < n and 0 <= y < n

def solve():
    global queue
    nxt     = []
    nxt_map = {}   # (x, y) -> index in nxt
    wave    = 1

    while queue:
        while queue:
            cur = queue.pop()
            cx, cy, cnum = cur

            for d in range(4):
                x = cx + dx[d]
                y = cy + dy[d]
                if not ok(x, y):
                    continue

                if grid[x][y] == 0:
                    grid[x][y] = MARKED if cnum == -1 else -cnum
                    idx = len(nxt)
                    nxt.append([x, y, cnum])
                    nxt_map[(x, y)] = idx
                    waves[x][y] = wave

                elif waves[x][y] == wave and grid[x][y] != -cnum and grid[x][y] != MARKED:
                    grid[x][y] = MARKED
                    idx = nxt_map.get((x, y))
                    if idx is not None:
                        nxt[idx][2] = -1

        queue, nxt = nxt, []
        nxt_map = {}
        wave += 1

def output():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == MARKED:
                grid[i][j] = 0
            elif grid[i][j] < 0:
                sx, sy = starts[-grid[i][j] - 1]
                grid[i][j] = grid[sx][sy]
            print(grid[i][j], end=' ')
        print()

solve()
output()
