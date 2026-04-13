MAX_VALUE = 10 ** 9


def main():
    str_ = input().strip()
    n = len(str_)
    mas = [[0] * n for _ in range(n)]

    open_ = "(["
    clos_ = ")]"

    def is_pair(f, s):
        pos_f = open_.find(f)
        pos_s = clos_.find(s)
        return pos_f == pos_s and pos_f != -1

    def pair(one):
        pos = open_.find(one)
        if pos == -1:
            pos = clos_.find(one)
        return open_[pos] + clos_[pos]

    def get_answer(l, r):
        if l > r:
            return ""
        if l == r:
            return pair(str_[l])

        border = mas[l + 1][r - 1] if is_pair(str_[l], str_[r]) else MAX_VALUE
        if border == mas[l][r]:
            return str_[l] + get_answer(l + 1, r - 1) + str_[r]

        for m in range(l, r):
            if mas[l][m] + mas[m + 1][r] == mas[l][r]:
                return get_answer(l, m) + get_answer(m + 1, r)
    for i in range(n):
        mas[i][i] = 1

    for length in range(1, n):
        for i in range(n):
            j = i + length
            if j >= n:
                break

            cur_len = MAX_VALUE
            if is_pair(str_[i], str_[j]):
                cur_len = mas[i + 1][j - 1]

            for m in range(i, j):
                cur_len = min(cur_len, mas[i][m] + mas[m + 1][j])

            mas[i][j] = cur_len
    answer = get_answer(0, n - 1)
    print(answer)


if __name__ == "__main__":
    main()
