import sys

data = sys.stdin.read().splitlines()
s = ''.join(data[0].split())
rules = []
for line in data[1:]:
    clean = ''.join(line.split())
    if '->' in clean:
        left, right = clean.split('->')
        rules.append((left, right))

seen = {}
steps = 0
while s not in seen:
    seen[s] = steps
    applied = False
    for left, right in rules:
        pos = s.find(left)
        if pos != -1:
            s = s[:pos] + right + s[pos + len(left):]
            steps += 1
            applied = True
            break
    if not applied:
        print(steps, 0)
        sys.exit(0)

st = seen[s]
dlina = steps - st
print(st, dlina)
