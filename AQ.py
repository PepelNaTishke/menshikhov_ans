import sys

vvod = sys.stdin.readline

def solve():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()

    reach = 0

    for x in nums:
        if x > reach + 1:
            break
        reach += x

    print(reach + 1)


solve()