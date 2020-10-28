def check_search_condition(target, rocks, n):
    removed_counter = 0

    index = 0
    prev_rock = 0
    while index < len(rocks):
        rock = rocks[index]
        distance = rock - prev_rock

        if distance < target:
            removed_counter += 1
        else:
            prev_rock = rock

        if removed_counter > n:
            break

        index += 1

    condition = removed_counter <= n
    return condition


def solution(distance, rocks, n):
    rocks = sorted(rocks + [distance])

    left = 1
    right = distance

    while left <= right:
        middle = (left + right) // 2

        move_to_right = check_search_condition(middle, rocks, n)
        if move_to_right:
            left = middle + 1
        else:
            right = middle - 1
    return right


if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    assert solution(distance, rocks, n) == 4
