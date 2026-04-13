import sys

eps = 1e-9

def fabs(a):
    return -a if a < 0 else a

def equal(a, b):
    return fabs(a - b) <= eps

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @staticmethod
    def from_input():
        x, y = map(float, sys.stdin.readline().split())
        return Point(x, y)

    def output(self):
        x = 0 if equal(self.x, 0) else self.x
        y = 0 if equal(self.y, 0) else self.y
        print(f"{x:.2f} {y:.2f}", end='')

def find_s(a, b, c):
    return 0.5 * (
        a.x * b.y + b.x * c.y + c.x * a.y
        - a.y * b.x - b.y * c.x - c.y * a.x
    )

def main():
    n = int(sys.stdin.readline())
    mas = [Point.from_input() for _ in range(n)]

    S = 0.0
    mid_x = 0.0
    mid_y = 0.0

    for i in range(1, n - 1):
        cur_s = find_s(mas[0], mas[i], mas[i + 1])
        S += cur_s
        mid_x += cur_s * (mas[0].x + mas[i].x + mas[i + 1].x) / 3
        mid_y += cur_s * (mas[0].y + mas[i].y + mas[i + 1].y) / 3

    center = Point(mid_x / S, mid_y / S)
    center.output()

if __name__ == "__main__":
    main()
