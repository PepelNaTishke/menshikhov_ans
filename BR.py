from math import gcd
from sys import stdin, stdout


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def input(self):
        line = stdin.readline().strip().split()
        self.x, self.y = int(line[0]), int(line[1])


def abs_val(a):
    return -a if a < 0 else a


def square(a, b, c):
    return (a.x * (b.y - c.y) +
            b.x * (c.y - a.y) +
            c.x * (a.y - b.y))


def find_border_points(mas, n):
    res = 0
    for i in range(n):
        j = (i + 1) % n
        dx = abs_val(mas[i].x - mas[j].x)
        dy = abs_val(mas[i].y - mas[j].y)
        res += gcd(dx, dy)
    return res


def main():
    n = int(stdin.readline().strip())
    mas = [Point() for _ in range(n)]

    for i in range(n):
        mas[i].input()
    S = 0
    for i in range(1, n - 1):
        S += square(mas[0], mas[i], mas[i + 1])
    S = abs_val(S) // 2
    border_points = find_border_points(mas, n)
    inside_points = S - border_points // 2 + 1
    stdout.write(str(inside_points) + '\n')


if __name__ == "__main__":
    main()
