f, s, n = map(int, input().split())
if f > s:
    f, s = s, f

bc = 0
br = n
max_s = n // s

for b in range(max_s + 1):
    rem = n - b * s
    a = rem // f
    rest = rem - a * f
    total = a + b
    if rest < br or (rest == br and total > bc):
        bc = total
        br = rest

if br != 0:
    print(bc, br)
else:
    print(bc)
