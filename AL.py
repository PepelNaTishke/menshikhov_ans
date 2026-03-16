s = input().strip()
n = len(s)
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    one = int(s[i - 1])
    if 0 <= one <= 9:
        dp[i] += dp[i - 1]
    if i >= 2:
        two = int(s[i - 2:i])
        if 10 <= two <= 33:
            dp[i] += dp[i - 2]

print(dp[n])