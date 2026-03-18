CHECK = '#'
UNCHECK = '.'

def correct(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(fx, fy, mas, n, m):
    stack = [(fx, fy)]
    move_x = [-1, 0, 1, 0]
    move_y = [0, -1, 0, 1]
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            x = cx + move_x[i]
            y = cy + move_y[i]
            if correct(x, y, n, m) and mas[x][y] == CHECK:
                mas[x][y] = UNCHECK
                stack.append((x, y))

def solve(n, m, mas):
    amount = 0
    for i in range(n):
        for j in range(m):
            if mas[i][j] == CHECK:
                dfs(i, j, mas, n, m)
                amount += 1
    print(amount)

n, m = map(int, input().split())
mas = [list(input()) for _ in range(n)]
solve(n, m, mas)