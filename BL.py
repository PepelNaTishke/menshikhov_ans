import math

def area(x1, y1, r1, x2, y2, r2):
    if r1 < r2:
        return area(x2, y2, r2, x1, y1, r1)
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d >= r1 + r2:
        return 0.0
    if d + r2 <= r1:
        return math.pi * r2 * r2
    alpha = 2 * math.acos((d*d + r1*r1 - r2*r2) / (2*d*r1))
    beta  = 2 * math.acos((d*d + r2*r2 - r1*r1) / (2*d*r2))
    return r1*r1 * (alpha - math.sin(alpha)) / 2 + r2*r2 * (beta - math.sin(beta)) / 2

x1, y1, r1, x2, y2, r2 = map(float, input().split())
print(f"{area(x1, y1, r1, x2, y2, r2):.3f}")
