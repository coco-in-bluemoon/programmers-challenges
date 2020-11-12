from itertools import combinations


def is_prime_number(number, cache):
    if number in cache:
        return cache[number]

    for divider in range(2, int(number ** 0.5) + 1):
        if not number % divider:
            cache[number] = False
            return False

    cache[number] = True
    return True


def solution(nums):
    counter = 0
    cache = dict()
    for combination in combinations(nums, 3):
        number = sum(combination)
        if is_prime_number(number, cache):
            counter += 1

    return counter


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    assert solution(nums) == 1

    nums = [1, 2, 7, 6, 4]
    assert solution(nums) == 4
