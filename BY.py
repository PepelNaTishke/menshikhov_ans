n, s = map(int, input().split())

def f(x):
    return x * (x - 1) // 2

amount = 0
for nz in range(n + 1):
    for m in range(nz + 1):
        plus = nz - m
        if f(m) + f(plus) - plus * m == s:
            amount += 1
            break

print(amount)
