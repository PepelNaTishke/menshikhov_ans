import sys

sys.setrecursionlimit(100000)

n = int(input())

mem = {}


def is_win(value):
    if value in mem:
        return mem[value]

    cur_win = -1
    for i in range(2, 10):
        if value * i >= n or is_win(value * i) == -1:
            cur_win = 1
            break

    mem[value] = cur_win
    return cur_win


if is_win(1) == 1:
    print("Stan wins.")
else:
    print("Ollie wins.")