import sys

Amount = [1,2,3,      # ABC
          1,2,3,      # DEF
          1,2,3,      # GHI
          1,2,3,      # JKL
          1,2,3,      # MNO
          1,2,3,4,    # PQRS
          1,2,3,      # TUV
          1,2,3,4]    # WXYZ

Button = [2,2,2,      # ABC
          3,3,3,      # DEF
          4,4,4,      # GHI
          5,5,5,      # JKL
          6,6,6,      # MNO
          7,7,7,7,    # PQRS
          8,8,8,      # TUV
          9,9,9,9]    # WXYZ

Len = [0] * 10
for b in Button:
    Len[b] += 1

def parse_str(init):
    mas = [0]
    for ch in init:
        idx = ord(ch) - ord('A')
        length = Amount[idx]
        for _ in range(length):
            mas.append(Button[idx])
    return mas

def solve(n, init):
    str_mas = parse_str(init)
    size = len(str_mas)
    mas = [[0] * size for _ in range(n + 1)]
    mas[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, size):
            mas[i][j] = mas[i-1][j-1]
            length = Len[str_mas[j]]
            for k in range(1, length):
                if j - k - 1 >= 0 and str_mas[j] == str_mas[j - k]:
                    mas[i][j] += mas[i-1][j-k-1]
                else:
                    break

    print(mas[n][size - 1])

data = sys.stdin.read().split()
n = int(data[0])
init = data[1]
solve(n, init)