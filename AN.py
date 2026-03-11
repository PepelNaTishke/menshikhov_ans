import math

def get_input():
    return map(int, input().split())

eps = 1e-8

def fabs(a):
    return -a if a < 0 else a

def equal(a, b):
    return fabs(a - b) <= eps

def less(a, b):
    return a < b and not equal(a, b)

def more(a, b):
    return a > b and not equal(a, b)

def is_round_double(a):
    return fabs(a - int(a + eps)) <= eps

def is_side_no_corner_y(cur_y):
    return cur_y != 0 and cur_y != N

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, f, s):
        self.a = s.y - f.y
        self.b = f.x - s.x
        self.c = -self.a * f.x - self.b * f.y

    def get_y(self, x):
        return (-self.a * x - self.c) / self.b

def solve():
    l = Line(Point(0, W), Point(100 * N, E))

    if l.a == 0:
        if W % 100 == 0 and W != 0 and W != 100 * N:
            print(2 * N)
        else:
            print(N)
        return

    cross_rect = 0
    prev_y = l.get_y(0) / 100

    if is_round_double(prev_y) and is_side_no_corner_y(prev_y):
        cross_rect += 1

    for x in range(1, N + 1):
        cur_y = l.get_y(100 * x) / 100

        if is_round_double(cur_y):
            if x != N:
                cross_rect += 2
            elif is_side_no_corner_y(cur_y):
                cross_rect += 1

        if int(cur_y + eps) != int(prev_y + eps):
            if more(prev_y, cur_y) and not is_round_double(prev_y):
                cross_rect += 1
            if less(prev_y, cur_y) and not is_round_double(cur_y):
                cross_rect += 1

        cross_rect += 1
        prev_y = cur_y

    print(cross_rect)

N, W, E = get_input()
solve()