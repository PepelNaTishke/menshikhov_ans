from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

class Fraction:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den
        self.norm()

    def norm(self):
        d = gcd(abs(self.num), abs(self.den))
        self.num //= d
        self.den //= d
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

    def __add__(self, o):
        d = lcm(self.den, o.den)
        return Fraction(d // self.den * self.num + d // o.den * o.num, d)

    def __sub__(self, o):
        d = lcm(self.den, o.den)
        return Fraction(d // self.den * self.num - d // o.den * o.num, d)

    def __mul__(self, o):
        return Fraction(self.num * o.num, self.den * o.den)

    def __truediv__(self, o):
        return Fraction(self.num * o.den, self.den * o.num)

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        whole = self.num // self.den
        if whole != 0:
            rem = abs(self.num) % self.den
            return f"{whole} {rem}/{self.den}"
        return f"{self.num}/{self.den}"

def parse(s):
    s = s.strip()
    if ' ' in s:
        parts = s.split(' ', 1)
        whole = int(parts[0])
        num, den = map(int, parts[1].split('/'))
        if den * whole < 0:
            num = -num + den * whole
        else:
            num = num + den * whole
        return Fraction(num, den)
    elif '/' in s:
        num, den = map(int, s.split('/'))
        return Fraction(num, den)
    else:
        return Fraction(int(s))

a = parse(input())
op = input().strip()
b = parse(input())

ops = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
print(ops[op])
