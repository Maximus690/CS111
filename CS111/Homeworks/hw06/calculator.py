from pair import Pair, nil
import re

def parse_tokens(tokens, index):
    t, i = tokens, index
    if t[i] == '(':
        op = t[i + 1]
        if i != 0:
            pair, i = parse_tokens(t, i + 2)
            op = Pair(op, pair)
        elif i == 0:
            i += 2
        pair, i = parse_tokens(t, i)
        return Pair(op, pair), i
    elif t[i] == ')':
        return nil, i + 1
    try:
        if '.' in t[i]:
            num = float(t[i])
        else:
            num = int(t[i])
        pair, i = parse_tokens(t, i + 1)
        return Pair(num, pair), i
    except ValueError:
        raise TypeError


def tokenize(expression):
    expression = expression.replace("(", " ( ").replace(')', " ) ")
    return expression.split()



