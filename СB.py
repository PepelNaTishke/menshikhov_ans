import math

k = 0.0008137
V0 = 800.0
m = 9.6
g = 9.8
pi = 2 * math.acos(0.0)


def input_data():
    alpha_deg = float(input())
    alpha_rad = pi * alpha_deg / 180.0
    return alpha_rad


def solve(alpha):
    dt = 0.0001

    Vxt = V0 * math.cos(alpha)
    Vyt = V0 * math.sin(alpha)
    Xt = Vxt * dt
    Yt = Vyt * dt

    while Yt >= 0:
        Vt = math.sqrt(Vxt * Vxt + Vyt * Vyt)

        Xnext = Xt + Vxt * dt
        Ynext = Yt + Vyt * dt

        Frt = k * Vt * Vt
        Frxt = - Frt * Vxt / Vt
        Fryt = - Frt * Vyt / Vt

        Axt = Frxt / m
        Ayt = Fryt / m - g

        Vxt = Vxt + Axt * dt
        Vyt = Vyt + Ayt * dt

        Xt = Xnext
        Yt = Ynext

    print(round(Xt))


def main():
    alpha = input_data()
    solve(alpha)


if __name__ == "__main__":
    main()
