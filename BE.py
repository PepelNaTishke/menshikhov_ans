def grundy(size, k, memo={}):
    if (size, k) in memo:
        return memo[(size, k)]
    if size < k:
        memo[(size, k)] = 0
        return 0
    reachable = set()
    for i in range(size - k + 1):
        left  = i
        right = size - i - k
        g = grundy(left, k, memo) ^ grundy(right, k, memo)
        reachable.add(g)
    mex = 0
    while mex in reachable:
        mex += 1
    memo[(size, k)] = mex
    return mex

n, k = map(int, input().split())
s = input().strip()
blocks = []
cnt = 0
for ch in s:
    if ch == 'O':
        cnt += 1
    else:
        if cnt > 0:
            blocks.append(cnt)
            cnt = 0
if cnt > 0:
    blocks.append(cnt)

if not blocks or all(b < k for b in blocks):
    print(0)
else:
    xor = 0
    for b in blocks:
        xor ^= grundy(b, k)
    print(1 if xor != 0 else 2)
