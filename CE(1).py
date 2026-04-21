import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)

    N = int(next(it))
    W = int(next(it))
    H = int(next(it))

    trees = []
    for _ in range(N):
        x = int(next(it))
        y = int(next(it))
        trees.append((x, y))
    xs = {0, W}
    ys = {0, H}
    for x, y in trees:
        xs.add(x)
        ys.add(y)

    max_L = min(W, H)
    for L in range(max_L, 0, -1):
        candidates = []
        for x in xs:
            P = x
            if 0 <= P <= W - L:
                candidates.append(P)
        candidates = sorted(set(candidates))

        for P in candidates:
            for Q in candidates:
                if Q < 0 or Q > H - L:
                    continue
                valid = True
                left = P
                right = P + L
                bottom = Q
                top = Q + L

                for x, y in trees:
                    if left < x < right and bottom < y < top:
                        valid = False
                        break

                if valid:
                    best_P, best_Q, best_L = P, Q, L
                    print(best_P, best_Q, best_L)
                    return
    print(0, 0, 0)

if __name__ == "__main__":
    main()
