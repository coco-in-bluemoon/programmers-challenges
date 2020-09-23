from itertools import permutations
import re
import sys


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def solution(expression):
    orig_numbers = re.findall(r'[0-9]+', expression)
    orig_operators = re.findall(r'[\+\-\*]', expression)

    answer = -sys.maxsize

    for priority in permutations('+-*', 3):
        numbers = [int(number) for number in orig_numbers]
        operators = orig_operators.copy()

        for operator in priority:
            while operator in operators:
                index = operators.index(operator)

                operators.pop(index)
                a = numbers.pop(index)
                b = numbers.pop(index)

                c = calculate(a, b, operator)
                numbers.insert(index, c)

        answer = max(answer, abs(numbers[0]))

    return answer


if __name__ == '__main__':
    expression = '100-200*300-500+20'
    assert solution(expression) == 60420

    expression = '50*6-3*2'
    assert solution(expression) == 300
