MAX_LEN = 10**9
def count_digits(num):
    if num == 0:
        return 1
    cnt = 0
    while num:
        num //= 10
        cnt += 1
    return cnt


def get_answer(i, j, s, mas):
    if i == j:
        return s[i]
    length = j - i + 1
    for step in range(1, length // 2 + 1):
        if length % step != 0:
            continue
        is_ok = True
        for cur in range(step):
            base = i + cur
            for pos in range(i + cur, j + 1, step):
                if s[base] != s[pos]:
                    is_ok = False
                    break
            if not is_ok:
                break
        if is_ok:
            times = length // step
            cur_len = count_digits(times) + 2 + mas[i][i + step - 1]
            if cur_len == mas[i][j]:
                block = get_answer(i, i + step - 1, s, mas)
                return str(times) + "(" + block + ")"
    for m in range(i, j):
        if mas[i][m] + mas[m + 1][j] == mas[i][j]:
            left = get_answer(i, m, s, mas)
            right = get_answer(m + 1, j, s, mas)
            return left + right
    return s[i:j + 1]


def solve(s):
    n = len(s)
    if n == 0:
        print("")
        return
    mas = [[MAX_LEN] * n for _ in range(n)]
    for length in range(n):
        for i in range(n):
            j = i + length
            if j >= n:
                break

            if length == 0:
                mas[i][j] = 1
            else:
                res = MAX_LEN
                total_len = j - i + 1
                for step in range(1, total_len // 2 + 1):
                    if total_len % step != 0:
                        continue
                    is_ok = True
                    for cur in range(step):
                        base = i + cur
                        for pos in range(i + cur, j + 1, step):
                            if s[base] != s[pos]:
                                is_ok = False
                                break
                        if not is_ok:
                            break
                    if is_ok:
                        times = total_len // step
                        cur_len = count_digits(times) + 2 + mas[i][i + step - 1]
                        res = min(res, cur_len)
                for m in range(i, j):
                    res = min(res, mas[i][m] + mas[m + 1][j])

                mas[i][j] = res

    ans = get_answer(0, n - 1, s, mas)
    print(ans, end="")


def main():
    s = input().strip()
    solve(s)


if __name__ == "__main__":
    main()
