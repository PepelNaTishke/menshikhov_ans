import math

def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)

def main():

    x1, y1, x2, y2, Dx, Dy = map(int, input().split())
    X_max = Dx + lcm(x1, x2)
    Y_max = Dy + lcm(y1, y2)

    x_lines = set()
    x = 0
    while x <= X_max:
        x_lines.add(x)
        x += x1
    x = Dx
    while x <= X_max:
        x_lines.add(x)
        x += x2

    y_lines = set()
    y = 0
    while y <= Y_max:
        y_lines.add(y)
        y += y1
    y = Dy
    while y <= Y_max:
        y_lines.add(y)
        y += y2


    xs = sorted(x_lines)
    ys = sorted(y_lines)


    areas: Set[int] = set()


    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            dx = xs[i + 1] - xs[i]
            dy = ys[j + 1] - ys[j]
            s = dx * dy
            if s > 0:
                areas.add(s)


    result = sorted(areas)

    print(len(result))
    for a in result:
        print(a)


main()
