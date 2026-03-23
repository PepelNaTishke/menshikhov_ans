import sys
import math

def solve():
    data = sys.stdin.read().split()
    n, s = int(data[0]), int(data[1])
    prev = [0] * (s + 1)
    prev[0] = 1
    
    for _ in range(n):
        prefix = [0] * (s + 2)
        for r in range(s + 1):
            prefix[r + 1] = prefix[r] + prev[r]
        
        curr = [0] * (s + 1)
        for r in range(1, s + 1):
            lo = r - 6 if r > 6 else 0
            curr[r] = prefix[r] - prefix[lo]
        
        prev = curr
    total = 6 ** n
    ways = prev[s]
    
    if ways <= 0:
        print("  0.00000000000000E+0000")
        return
    log_result = math.log10(ways) - math.log10(total)
    exp = int(math.floor(log_result))
    mantissa = 10 ** (log_result - exp)
    
    print(f" {mantissa:.14f}E{exp:+05d}")

solve()
