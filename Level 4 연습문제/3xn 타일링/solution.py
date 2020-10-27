import sys
sys.setrecursionlimit(10**5)


# f(N) = 3*f(N-2) + 2*f(N-4) + 2*f(N-6) + 2*f(2) + 2
def get_possible_blocks(n, memo):
    if not n:
        return 2

    if n in memo:
        return memo[n]

    base = n-2
    counter = 3 * get_possible_blocks(base, memo)
    counter = (counter % 1000000007)
    while base > 2:
        base -= 2
        counter += (2 * get_possible_blocks(base, memo))
        counter = (counter % 1000000007)
    counter += 2
    counter = (counter % 1000000007)
    memo[n] = counter
    return counter


def solution(n):
    if n % 2:
        return 0
    memo = {2: 3}
    answer = get_possible_blocks(n, memo)
    return answer


if __name__ == "__main__":
    assert solution(4) == 11
    assert solution(8) == 153
