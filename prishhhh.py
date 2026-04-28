# а) Spiral fill
def spiral(n, m):
    a = [[0]*m for _ in range(n)]
    top, bot, lft, rgt = 0, n-1, 0, m-1
    num = 1
    while top <= bot and lft <= rgt:
        for j in range(lft, rgt+1): a[top][j] = num; num+=1
        top += 1
        for i in range(top, bot+1): a[i][rgt] = num; num+=1
        rgt -= 1
        for j in range(rgt, lft-1, -1): a[bot][j] = num; num+=1
        bot -= 1
        for i in range(bot, top-1, -1): a[i][lft] = num; num+=1
        lft += 1
    return a

# б) Diagonal snake fill
def diagonal(n, m):
    a = [[0]*m for _ in range(n)]
    num = 1
    for s in range(n + m - 1):
        if s % 2 == 0:  # going up-right
            r, c = min(s, n-1), s - min(s, n-1)
            while r >= 0 and c < m:
                a[r][c] = num; num+=1
                r -= 1; c += 1
        else:            # going down-left
            c, r = min(s, m-1), s - min(s, m-1)
            while c >= 0 and r < n:
                a[r][c] = num; num+=1
                r += 1; c -= 1
    return a

# в) Column snake fill
def col_snake(n, m):
    a = [[0]*m for _ in range(n)]
    num = 1
    for j in range(m):
        if j % 2 == 0:
            for i in range(n): a[i][j] = num; num+=1
        else:
            for i in range(n-1, -1, -1): a[i][j] = num; num+=1
    return a

def show(a):
    for row in a: print(row)

print("а) Spiral 3x4:"); show(spiral(3,4)); print()
print("б) Diagonal 3x4:"); show(diagonal(3,4)); print()
print("в) Column snake 3x4:"); show(col_snake(3,4))
