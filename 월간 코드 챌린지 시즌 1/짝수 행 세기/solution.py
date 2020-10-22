import math
from math import comb


def calculate_combination(n, r, combinations):
    if combinations[n][r]:
        return combinations[n][r]
    combinations[n][r] = comb(n, r)
    return combinations[n][r]


def solution(a):
    MOD = 10**7 + 19
    R = len(a)
    C = len(a[0])

    dp = [[0] * (R+1) for _ in range(C)]

    counter_one = {c: 0 for c in range(C)}
    for r in range(R):
        for c in range(C):
            counter_one[c] += a[r][c]

    combinations = [[0] * (R+1) for _ in range(R+1)]

    num_one = counter_one[0]
    num_zero = R - num_one
    dp[0][num_zero] = calculate_combination(R, num_zero, combinations)

    for c in range(1, C):
        for num_even, freq in enumerate(dp[c-1]):
            if not freq:
                continue
            num_one = counter_one[c]
            num_odd = R - num_even
            for k in range(num_one+1):
                new_num_even_from_even = num_even - k
                if new_num_even_from_even < 0:
                    continue

                k_left = num_one - k
                new_num_even_from_odd = k_left
                if new_num_even_from_odd > num_odd:
                    continue

                new_num_even =\
                    new_num_even_from_even + new_num_even_from_odd

                combination_from_even =\
                    calculate_combination(num_even, k, combinations)
                combination_from_odd = \
                    calculate_combination(num_odd, k_left, combinations)
                combination = combination_from_even * combination_from_odd
                dp[c][new_num_even] += ((freq * combination) % MOD)

    return dp[C-1][R]


if __name__ == "__main__":
    a = [
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    assert solution(a) == 6

    a = [
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert solution(a) == 0

    a = [
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    assert solution(a) == 72
