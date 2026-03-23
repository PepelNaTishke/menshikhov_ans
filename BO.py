SIZE = 1010

mas = [0] * SIZE
mem = {}
pos = {}

a, b, c = map(int, input().split())
mas[0], mas[1], mas[2] = a, b, c
mem[mas[2] + 10*mas[1] + 100*mas[0]] = 1

n = int(input()) - 1

base = -1
length = -1

for i in range(3, SIZE):
    mas[i] = (mas[i-1] + mas[i-2] + mas[i-3]) % 10
    val = mas[i-1] + 10*mas[i-2] + 100*mas[i-3]
    if val in mem and i != 3:
        base = pos[val]
        length = i - 3 - base
        break
    mem[val] = 1
    pos[val] = i - 3

if n < base + length:
    print(mas[n])
else:
    print(mas[base + (n - base) % length])
