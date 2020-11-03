def check_validity(target, stones, k):
    counter_skip = 0

    for stone in stones:
        if stone < target:
            counter_skip += 1
        else:
            counter_skip = 0

        if counter_skip >= k:
            return False

    return True


def solution(stones, k):
    left = min(stones)
    right = max(stones)

    while left <= right:
        middle = (left + right) // 2

        if check_validity(middle, stones, k):
            left = middle + 1
        else:
            right = middle - 1

    return right


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    assert solution(stones, k) == 3
