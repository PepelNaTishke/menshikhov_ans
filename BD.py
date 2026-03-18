def precalc():
    mas = ["A", "B"]
    for i in range(2, 10):
        mas.append(mas[i-1] + mas[i-2])
    return mas

def intersect(N, s, mas):
    pos = N - 1
    while pos >= len(mas):
        pos -= 2
    beg = mas[pos]
    end = mas[N-2] if N-2 < len(mas) else mas[-1]

    common = beg + end
    left  = max(len(beg) - len(s) + 1, 0)
    right = min(len(beg) - 1, len(common) - len(s))

    for i in range(left, right + 1):
        if common[i:i + len(s)] == s:
            return 1
    return 0

n = int(input())
s = input()
mas = precalc()
calc = [0] * n

if s == "A":
    calc[0] = 1
if n > 1 and s == "B":
    calc[1] = 1

for i in range(2, n):
    calc[i] = calc[i-1] + calc[i-2] + intersect(i, s, mas)

print(calc[-1])
