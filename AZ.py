import math
import sys
sys.setrecursionlimit(100000)

EPS = 1e-8

def fabs(a):
    return -a if a < 0 else a

def eq(a, b):
    return fabs(a - b) <= EPS

def lt(a, b):
    return not eq(a, b) and a < b

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    def __init__(self, p, q):
        self.a = q.y - p.y
        self.b = p.x - q.x
        self.c = -(self.a * p.x + self.b * p.y)

    def dist(self, p):
        n = math.sqrt(self.a**2 + self.b**2)
        return fabs(self.a * p.x + self.b * p.y + self.c) / n if n > EPS else 0.0

    def left(self, p):
        return lt(self.a * p.x + self.b * p.y + self.c, 0)

    def right(self, p):
        return lt(0, self.a * p.x + self.b * p.y + self.c)


def get_left(pts, ids, ln):
    return [i for i in ids if ln.left(pts[i])]

def qhull(pts, hull, li, ri, ids):
    if not ids:
        hull.append(ri)
        return

    base = Line(pts[li], pts[ri])
    top = ids[0]
    topln = Line(pts[li], pts[top])
    best = base.dist(pts[top])

    for i in ids[1:]:
        if i != li and i != ri:
            d = base.dist(pts[i])
            if eq(best, d):
                if topln.left(pts[i]):
                    top = i
                    topln = Line(pts[li], pts[top])
            elif lt(best, d):
                best = d
                top = i
                topln = Line(pts[li], pts[top])

    ln1 = Line(pts[li], pts[top])
    qhull(pts, hull, li, top, get_left(pts, ids, ln1))

    ln2 = Line(pts[top], pts[ri])
    qhull(pts, hull, top, ri, get_left(pts, ids, ln2))

def hull(pts):
    res = []
    if len(pts) < 3:
        return res

    li = min(range(len(pts)), key=lambda i: pts[i].x)
    ri = max(range(len(pts)), key=lambda i: pts[i].x)

    mid = Line(pts[li], pts[ri])
    up, dn = [], []

    for i in range(len(pts)):
        if i != li and i != ri:
            if mid.left(pts[i]):
                up.append(i)
            elif mid.right(pts[i]):
                dn.append(i)

    qhull(pts, res, li, ri, up)
    qhull(pts, res, ri, li, dn)
    return res

def tri(a, b, c):
    return a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)

def area(pts, h):
    s = 0.0
    for i in range(1, len(h) - 1):
        s += tri(pts[h[0]], pts[h[i]], pts[h[i+1]])
    return fabs(s / 2)

def dfs(cur, rivers, used, pts):
    for nxt in range(len(rivers)):
        if not used[nxt]:
            ok = (rivers[nxt][-1] in rivers[cur] or
                  rivers[cur][-1] in rivers[nxt])
            if ok:
                used[nxt] = True
                pts.extend(rivers[nxt])
                dfs(nxt, rivers, used, pts)

def solve():
    n = int(input())
    rivers = []
    for _ in range(n):
        k = int(input())
        pts = [Point(*map(float, input().split())) for _ in range(k)]
        rivers.append(pts)

    used = [False] * n
    best = 0.0

    for i in range(n):
        if not used[i]:
            used[i] = True
            pts = list(rivers[i])
            dfs(i, rivers, used, pts)
            s = area(pts, hull(pts))
            if s > best:
                best = s

    print(f"{best:.2f}")

solve()
