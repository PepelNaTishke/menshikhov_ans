import math

a, b = map(int, input().split())
c, d = map(int, input().split())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

possible = False

steps = 100000
for i in range(steps + 1):
    theta = math.pi / 2 * i / steps
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    w = a * cos_t + b * sin_t
    h = a * sin_t + b * cos_t
    if w <= c + 1e-9 and h <= d + 1e-9:
        possible = True
        break

print("Possible" if possible else "Impossible")
