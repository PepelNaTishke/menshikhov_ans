import sys

EMPTY = 2

def input_data():
    global n, adj, results
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    adj = [[] for _ in range(n)]
    results = [EMPTY] * n

    for i in range(1, n):
        type_ = data[idx]; idx += 1
        parent = int(data[idx]) - 1; idx += 1
        adj[parent].append(i)
        if type_ == 'L':
            results[i] = int(data[idx]); idx += 1

def best_for(pl, vr):
    if results[vr] != EMPTY:
        return results[vr]
    is_draw = False
    for child in adj[vr]:
        cur = best_for(-pl, child)
        if cur == pl:
            return cur
        elif cur == 0:
            is_draw = True
    return 0 if is_draw else -pl

def solve():
    result = best_for(1, 0)
    print("+1" if result == 1 else result)

input_data()
solve()