from collections import defaultdict

def parse_filename(full_name):
    pos = full_name.find('.')
    if pos == -1:
        return full_name, ""
    else:
        return full_name[:pos], full_name[pos+1:]

def del_item(lst, value):
    if value in lst:
        lst.remove(value)

def check(m_primary, primary, m_secondary, secondary):
    for i in range(n - 1, -1, -1):
        group = m_primary[primary[i]]
        if group:
            if len(group) == 1:
                del_item(m_primary[primary[i]], i)
                del_item(m_secondary[secondary[i]], i)

def solve():
    for i in range(m):
        if i % 2 == 1:
            check(m_name, name, m_exp, exp)
        else:
            check(m_exp, exp, m_name, name)

def find_answer(is_output):
    amount = 0
    for i in range(n):
        if m_name[name[i]] and m_exp[exp[i]]:
            amount += 1
            if is_output:
                print(full_name[i])
    return amount

n, m = map(int, input().split())

full_name = []
name = []
exp = []
m_name = defaultdict(list)
m_exp  = defaultdict(list)

for i in range(n):
    s = input().strip()
    sname, sexp = parse_filename(s)
    full_name.append(s)
    name.append(sname)
    exp.append(sexp)
    m_name[sname].append(i)
    m_exp[sexp].append(i)

solve()
print(find_answer(False))
find_answer(True)
