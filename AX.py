n, s = map(int, input().split())

mem = [[0.0] * (n + 1) for _ in range(s + 1)]
mem[0][0] = 1.0

for i in range(1, n + 1):
    for r in range(1, s + 1):
        for prev in range(1, 7):
            if r - prev >= 0:
                mem[r][i] += mem[r - prev][i - 1] / 6.0

result = mem[s][n]

mantissa = result
exp = 0
if result > 0:
    import math
    exp = int(math.floor(math.log10(result)))
    mantissa = result / (10 ** exp)

print(f" {mantissa:.14f}E{exp:+05d}")
