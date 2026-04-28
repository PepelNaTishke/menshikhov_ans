n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
top, bot, lft, rgt = 0, n-1, 0, m-1
num = 1
while top <= bot and lft <= rgt:
    for j in range(lft, rgt+1): a[top][j] = num; num+=1
    top += 1
    for i in range(top, bot+1): a[i][rgt] = num; num+=1
    rgt -= 1
    if top <= bot:
        for j in range(rgt, lft-1, -1): a[bot][j] = num; num+=1
        bot -= 1
    if lft <= rgt:
        for i in range(bot, top-1, -1): a[i][lft] = num; num+=1
        lft += 1
for row in a:
    print(*row)
