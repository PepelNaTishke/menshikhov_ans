from math import gcd

n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]

amount = n
for i in range(n):
    x1, y1 = pts[i]
    x2, y2 = pts[(i+1) % n]
    amount += gcd(abs(x1-x2), abs(y1-y2)) - 1

print(amount)
