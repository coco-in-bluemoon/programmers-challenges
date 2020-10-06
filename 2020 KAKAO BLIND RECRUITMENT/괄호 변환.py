from collections import defaultdict
from collections import deque


def valid_parenthesis(p):
    stack = deque()

    for ch in p:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                return False

    return True if not stack else False


def split_parenthesis(p):
    counter = defaultdict(int)
    idx = 0

    while idx < len(p):
        ch = p[idx]

        key = 'open' if ch == '(' else 'close'
        counter[key] += 1

        if counter['open'] == counter['close']:
            break

        idx += 1

    return p[:idx+1], p[idx+1:]


def reverse_parenthesis(p):
    p = p.replace('(', '.')
    p = p.replace(')', '(')
    p = p.replace('.', ')')

    return p


def correct_parenthesis(p):
    if not p:
        return p

    u, v = split_parenthesis(p)

    if valid_parenthesis(u):
        v = correct_parenthesis(v)
        return u + v

    v = correct_parenthesis(v)
    u = reverse_parenthesis(u[1:-1])
    return '(' + v + ')' + u


def solution(p):
    p = correct_parenthesis(p)
    return p


if __name__ == "__main__":
    p = '(()())()'
    assert solution(p) == '(()())()'

    p = ')('
    assert solution(p) == '()'

    p = '()))((()'
    assert solution(p) == '()(())()'
