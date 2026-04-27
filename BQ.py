n = int(input())
a = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i + 1, j):
            cost = (dp[i][k] if i < k else 0) + (dp[k][j] if k < j else 0) + a[i] * a[k] * a[j]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n-1])
