from collections import defaultdict
import math


def calculate_min_value(arr, memo):
    if len(arr) == 1:
        return int(arr[0])

    key = ' '.join(arr) + 'MIN'
    if key in memo:
        return memo[key]

    value = math.inf
    for index in range(1, len(arr), 2):
        operator = arr[index]

        if operator == '+':
            left_value = calculate_min_value(arr[:index], memo)
            right_value = calculate_min_value(arr[index+1:], memo)
            value = min(value, left_value + right_value)
        elif operator == '-':
            left_value = calculate_min_value(arr[:index], memo)
            right_value = calculate_max_value(arr[index+1:], memo)
            value = min(value, left_value - right_value)

    memo[key] = value
    return value


def calculate_max_value(arr, memo):
    if len(arr) == 1:
        return int(arr[0])

    key = ' '.join(arr) + 'MAX'
    if key in memo:
        return memo[key]

    value = -math.inf
    for index in range(1, len(arr), 2):
        operator = arr[index]

        if operator == '+':
            left_value = calculate_max_value(arr[:index], memo)
            right_value = calculate_max_value(arr[index+1:], memo)
            value = max(value, left_value + right_value)
        elif operator == '-':
            left_value = calculate_max_value(arr[:index], memo)
            right_value = calculate_min_value(arr[index+1:], memo)
            value = max(value, left_value - right_value)

    memo[key] = value
    return value


def solution(arr):
    memo = defaultdict(int)
    answer = calculate_max_value(arr, memo)
    return answer


if __name__ == "__main__":
    arr = ['1', '-', '3', '+', '5', '-', '8']
    assert solution(arr) == 1

    arr = ['5', '-', '3', '+', '1', '+', '2', '-', '4']
    assert solution(arr) == 3
