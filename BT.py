from collections import defaultdict
import sys


def parse_formula(formula_str):
    formula = defaultdict(int)

    def read_number(pos):
        num = 0
        while pos[0] < len(formula_str) and formula_str[pos[0]].isdigit():
            num = num * 10 + int(formula_str[pos[0]])
            pos[0] += 1
        return num if num > 0 else 1

    def read_chem_element(pos):
        el = formula_str[pos[0]]
        pos[0] += 1
        if pos[0] < len(formula_str) and formula_str[pos[0]].islower():
            el += formula_str[pos[0]]
            pos[0] += 1
        return el

    def read_element(pos, number, local_formula):
        if formula_str[pos[0]] == '(':
            pos[0] += 1
            read_sequence(pos, number, local_formula)
            pos[0] += 1
        else:
            chem_element = read_chem_element(pos)
            local_formula[chem_element] += 1

    def read_sequence(pos, number, total_formula):
        local_formula = defaultdict(int)
        while pos[0] < len(formula_str) and (formula_str[pos[0]].isupper() or formula_str[pos[0]] == '('):
            local_formula.clear()
            read_element(pos, number, local_formula)
            mul = read_number(pos) if pos[0] < len(formula_str) and formula_str[pos[0]].isdigit() else 1
            for el, cnt in local_formula.items():
                total_formula[el] += cnt * mul

    def read_formula(pos):
        while pos[0] < len(formula_str):
            number = read_number(pos) if formula_str[pos[0]].isdigit() else 1
            seq_formula = defaultdict(int)
            if pos[0] < len(formula_str) and (formula_str[pos[0]].isupper() or formula_str[pos[0]] == '('):
                read_sequence(pos, number, seq_formula)
            for el, cnt in seq_formula.items():
                formula[el] += cnt * number
            if pos[0] < len(formula_str) and formula_str[pos[0]] == '+':
                pos[0] += 1
            else:
                break

    pos = [0]
    read_formula(pos)
    return dict(formula)
data = sys.stdin.read().strip().split('\n')
left_formula = data[0]
n = int(data[1])
right_formulas = data[2:2 + n]
left_counts = parse_formula(left_formula)
for right_formula in right_formulas:
    right_counts = parse_formula(right_formula)
    if left_counts == right_counts:
        print(f"{left_formula}=={right_formula}")
    else:
        print(f"{left_formula}!={right_formula}")
