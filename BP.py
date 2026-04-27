n, A = map(float, input().split())
n = int(n)

eps = 1e-9
h = [0.0] * n
h[0] = A


def fabs(a):
    return -a if a < 0 else a


def equal(a, b):
    return fabs(a - b) <= eps


def less(a, b):
    return a < b and not equal(a, b)


def more(a, b):
    return a > b and not equal(a, b)


def check(mid):
    h[1] = mid
    h[-1] = 0.0

    for i in range(2, n):
        h[i] = 2 * h[i - 1] - h[i - 2] + 2
        if not more(h[i], 0.0):
            return True

    return not more(h[-1], 0.0)


def solve():
    l = 0.0
    r = h[0]
    res = 1e9

    while less(l, r):
        mid = (l + r) / 2
        if check(mid):
            l = mid
        else:
            r = mid
            res = min(res, h[-1])

    print(f"{res:.2f}")


solve()
