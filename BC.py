n = int(input())
mas = list(range(1, n + 1))

for i in range(2, n):
    mas[i], mas[i // 2] = mas[i // 2], mas[i]

print(*mas)
