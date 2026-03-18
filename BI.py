a1, n = map(int, input().split())

seen = {}
seq = [a1]
cur = a1

for i in range(1, n):
    if cur in seen:
        start = seen[cur]
        cycle = i - start
        idx = (n - 1 - start) % cycle
        print(seq[start + idx])
        break
    seen[cur] = i - 1
    cur = (cur * cur) % 10000
    seq.append(cur)
else:
    print(seq[n - 1])
