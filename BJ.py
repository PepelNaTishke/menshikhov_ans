n, k = map(int, input().split())
wires = [int(input()) for _ in range(n)]

lo, hi = 1, max(wires)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = sum(w // mid for w in wires)
    if count >= k:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
