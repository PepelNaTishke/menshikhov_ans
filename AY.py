def solve():
    data = list(map(int, input().split()))
    n = data[0]
    mas = data[1:n+1]
    k = data[n+1]

    sums = [0] * n
    sums[0] = mas[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + mas[i]

    def range_sum(f, s):
        if f > s:
            return 0
        return sums[s] - (sums[f-1] if f > 0 else 0)

    keep  = [[0] * (n + 2) for _ in range(k)]
    leave = [[0] * (n + 2) for _ in range(k)]

    keep[0][n-1] = mas[n-1]
    for j in range(n-2, -1, -1):
        keep[0][j]  = (keep[0][j+2] if j+2 <= n-1 else 0) + mas[j]
        leave[0][j] = keep[0][j+1]

    for i in range(1, k):
        for j in range(n-1, -1, -1):
            max_up_keep = 0
            pos_up = 0
            for p in range(i-1, -1, -1):
                if max_up_keep < keep[p][j]:
                    max_up_keep = keep[p][j]
                    pos_up = p

            last = min(j + i, n - 1)
            max_right_keep = range_sum(j, last) + leave[i][last + 1]

            if max_up_keep > max_right_keep:
                keep[i][j]  = keep[pos_up][j]
                leave[i][j] = leave[pos_up][j]
            else:
                keep[i][j]  = max_right_keep
                leave[i][j] = keep[i][last + 1]

    print(keep[k-1][0])

solve()
