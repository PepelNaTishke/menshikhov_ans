s = input().strip()
n = len(s)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]

print(dp[0][n-1])
