n = int(input())
mas = sorted(map(int, input().split()))

if mas[0] != 1:
    print(1)
else:
    max_val = 1
    for i in range(1, n):
        if mas[i] <= max_val + 1:
            max_val += mas[i]
        else:
            break
    print(max_val + 1)