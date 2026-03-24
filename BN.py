from math import gcd

def parse_fraction(s):
    """Парсит дробь и возвращает (числитель, знаменатель)."""
    s = s.strip()
    negative = s.startswith('-')
    if negative:
        s = s[1:]

    if ' ' in s:
        # Формат: "целая числитель/знаменатель"
        whole_str, frac_str = s.split(' ', 1)
        whole = int(whole_str)
        num, den = map(int, frac_str.split('/'))
        num = whole * den + num
    elif '/' in s:
        # Формат: "числитель/знаменатель"
        num, den = map(int, s.split('/'))
    else:
        # Целое число
        num = int(s)
        den = 1

    if negative:
        num = -num

    return num, den


def format_fraction(num, den):
    """Форматирует дробь num/den в нужный формат."""
    if den < 0:
        num, den = -num, -den

    g = gcd(abs(num), den)
    num //= g
    den //= g

    negative = num < 0
    num = abs(num)

    whole = num // den
    remainder = num % den

    result = ''
    if negative and (whole > 0 or remainder > 0):
        result += '-'

    if remainder == 0:
        result += str(whole)
    else:
        if whole > 0:
            result += str(whole) + ' '
        result += f'{remainder}/{den}'

    return result


def apply_op(n1, d1, op, n2, d2):
    if op == '+':
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = d1 * n2
    return num, den


line1 = input()
op = input().strip()
line2 = input()

n1, d1 = parse_fraction(line1)
n2, d2 = parse_fraction(line2)

num, den = apply_op(n1, d1, op, n2, d2)
print(format_fraction(num, den))
