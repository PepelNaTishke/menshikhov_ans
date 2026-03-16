from math import gcd

n = int(input())
sp = []

for d in range(2, n + 1):
    for num in range(1, d):
        if gcd(num, d) == 1:
            sp.append((num, d))

sp.sort(key=lambda x: x[0] / x[1])

for num, d in sp:
    print(f"{num}/{d}")