def get_number_of_parenthesis(num, memo):
    if num in memo:
        return memo[num]

    counter = 0
    for left in range(num):
        right = num - left - 1
        left_counter = get_number_of_parenthesis(left, memo)
        right_counter = get_number_of_parenthesis(right, memo)
        counter += (left_counter * right_counter)
    memo[num] = counter

    return counter


def calculate_factorial(num, memo):
    if num in memo:
        return memo[num]
    factorial = num * calculate_factorial(num-1, memo)
    memo[num] = factorial
    return factorial


def calculate_catalan_number(n, memo):
    numerator = calculate_factorial(2 * n, memo)
    denominator = calculate_factorial(n, memo) * calculate_factorial(n+1, memo)
    catalan = numerator // denominator
    return catalan


def solution(n):
    memo = {0: 1, 1: 1}
    answer = get_number_of_parenthesis(n, memo)
    return answer


if __name__ == "__main__":
    assert solution(2) == 2
    assert solution(3) == 5
    assert solution(4) == 14
    assert solution(5) == 42
