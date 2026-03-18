from collections import deque

w, h = map(int, input().split())
grid = [list(input()) for _ in range(h)]
padded = [['.' ] * (w + 2)] + [['.' ] + row + ['.'] for row in grid] + [['.' ] * (w + 2)]
ph, pw = h + 2, w + 2

piece_id  = [[-1] * pw for _ in range(ph)]
hole_id   = [[-1] * pw for _ in range(ph)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def ok(x, y):
    return 0 <= x < ph and 0 <= y < pw

def bfs_fill(sx, sy, grid, visited, val, check):
    area = 0
    q = deque([(sx, sy)])
    visited[sx][sy] = val
    while q:
        cx, cy = q.popleft()
        area += 1
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if ok(nx, ny) and visited[nx][ny] == -1 and grid[nx][ny] == check:
                visited[nx][ny] = val
                q.append((nx, ny))
    return area
pieces = []
pid = 0
for i in range(ph):
    for j in range(pw):
        if padded[i][j] == '*' and piece_id[i][j] == -1:
            area = bfs_fill(i, j, padded, piece_id, pid, '*')
            pieces.append((pid, area))
            pid += 1

outer = [[-1] * pw for _ in range(ph)]
bfs_fill(0, 0, padded, outer, 0, '.')

holes = []
hid = 0
hole_map = [[-1] * pw for _ in range(ph)]
for i in range(ph):
    for j in range(pw):
        if padded[i][j] == '.' and outer[i][j] == -1 and hole_map[i][j] == -1:
            q = deque([(i, j)])
            hole_map[i][j] = hid
            pts = [(i, j)]
            while q:
                cx, cy = q.popleft()
                for d in range(4):
                    nx, ny = cx + dx[d], cy + dy[d]
                    if ok(nx, ny) and padded[nx][ny] == '.' and outer[nx][ny] == -1 and hole_map[nx][ny] == -1:
                        hole_map[nx][ny] = hid
                        q.append((nx, ny))
                        pts.append((nx, ny))
            holes.append((hid, pts))
            hid += 1

piece_holes = [0] * pid
for hid, pts in holes:
    owner = -1
    for (i, j) in pts:
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if ok(ni, nj) and padded[ni][nj] == '*':
                owner = piece_id[ni][nj]
                break
        if owner != -1:
            break
    if owner != -1:
        piece_holes[owner] += 1
max_holes = max(piece_holes) if piece_holes else 0

if max_holes == 0:
    print(0)
else:
    best = min(area for pid, area in pieces if piece_holes[pid] == max_holes)
    print(best)
