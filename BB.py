from collections import deque

def solve():
    n = int(input())
    rects = []
    xs = []
    ys = []

    for _ in range(n):
        x0, y0, x1, y1 = map(int, input().split())
        if x0 > x1: x0, x1 = x1, x0
        if y0 > y1: y0, y1 = y1, y0
        rects.append((x0, y0, x1, y1))
        xs += [x0, x1]
        ys += [y0, y1]

    xs = sorted(set(xs))
    ys = sorted(set(ys))
    N = len(xs) - 1
    M = len(ys) - 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def ok(x, y):
        return 0 <= x < N and 0 <= y < M

    adj = [[None] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cx0, cy0, cx1, cy1 = xs[i], ys[j], xs[i+1], ys[j+1]
            owners = []
            for k, (rx0, ry0, rx1, ry1) in enumerate(rects):
                if rx0 <= cx0 and cx1 <= rx1 and ry0 <= cy0 and cy1 <= ry1:
                    owners.append(k)
            adj[i][j] = tuple(owners)

    used = [[False] * M for _ in range(N)]

    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        while q:
            cx, cy = q.popleft()
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if ok(nx, ny) and not used[nx][ny] and adj[sx][sy] == adj[nx][ny]:
                    used[nx][ny] = True
                    q.append((nx, ny))

    count = 1
    for i in range(N):
        for j in range(M):
            if not used[i][j]:
                used[i][j] = True
                if adj[i][j]:
                    count += 1
                bfs(i, j)

    print(count)

solve()
