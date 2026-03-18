MAX_VALUE = 1 << 30

f, s, n = map(int, input().split())

if f > s:
    f, s = s, f

amounts = [0] * (n + 1)
rest    = [MAX_VALUE] * (n + 1)

for i in range(f):
    amounts[i] = 0
    rest[i]    = i

def go(step):
    for i in range(step, n + 1):
        if rest[i - step] < rest[i]:
            rest[i]    = rest[i - step]
            amounts[i] = amounts[i - step] + 1

go(f)
if f != s:
    go(s)

if rest[n] != 0:
    print(amounts[n], rest[n])
else:
    print(amounts[n])
