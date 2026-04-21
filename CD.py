import math

def det5(M):
    n = 5
    A = [row[:] for row in M]  # копия
    det = 1.0
    for i in range(n):
        if A[i][i] == 0:
            k = -1
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    k = j
                    break
            if k == -1:
                return 0.0
            A[i], A[k] = A[k], A[i]
            det = -det
        det *= A[i][i]
        for j in range(i + 1, n):
            if A[j][i] != 0:
                r = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= r * A[i][k]
    return det

a, b, c, d, e, f = map(int, input().split())
a2, b2, c2, d2, e2, f2 = a*a, b*b, c*c, d*d, e*e, f*f

M = [
    [0, 1,    1,    1,    1   ],
    [1, 0,    a2,   b2,   c2  ],
    [1, a2,   0,    d2,   e2  ],
    [1, b2,   d2,   0,    f2  ],
    [1, c2,   e2,   f2,   0   ]
]

det_val = det5(M)

if det_val <= 0:
    vol = 0.0
else:
    vol = math.sqrt(det_val) / (12 * math.sqrt(2))

print(f"{vol:.4f}")
