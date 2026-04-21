n, s = map(int, input().split())

ans = 0
for nz in range(n + 1):
    rest = n - nz
    if rest == 0:
        if s == 0:
            ans += 1
        continue

    R = rest * (rest - 1) - 2 * s
    if R < 0 or R % 4 != 0:
        continue

    T = R // 4

    D = rest * rest - 4 * T
    if D < 0:
        continue
    sd = int(D**0.5 + 0.5)
    if sd * sd != D:
        continue
    m1 = (rest - sd) // 2
    m2 = (rest + sd) // 2
    for m in [m1, m2]:
        if m < 0 or m > rest:
            continue
        p = rest - m
        total = m * (m - 1) // 2 + p * (p - 1) // 2 - m * p
        if total == s:
            ans += 1
            break

print(ans)
