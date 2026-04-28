n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
val = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = val
            val += 1
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = val
            val += 1

for row in matrix:
    print(*row)
