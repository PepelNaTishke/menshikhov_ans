import sys

def fib(prev, cur, i, n):
    if n > i:
        for _ in range(i + 2, n + 1):
            prev += cur
            prev, cur = cur, prev
        return cur
    else:
        for _ in range(i - 1, n - 1, -1):
            cur -= prev
            cur, prev = prev, cur
        return prev

def solve():
    data = input().split()
    i, Fi, j, Fj, n = int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])

    if n == i:
        print(Fi)
        return
    if n == j:
        print(Fj)
        return

    if i > j:
        i, j = j, i
        Fi, Fj = Fj, Fi

    if j == i + 1:
        print(fib(Fi, Fj, i, n))
        return

    l, r = -2_000_000_010, 2_000_000_010
    while l <= r:
        FiNxt = (l + r) // 2
        FjPos = fib(Fi, FiNxt, i, j)
        if FjPos < Fj:
            l = FiNxt + 1
        elif FjPos > Fj:
            r = FiNxt - 1
        else:
            print(fib(Fi, FiNxt, i, n))
            return

solve()
