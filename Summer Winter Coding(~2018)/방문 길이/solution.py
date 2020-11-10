from collections import deque


def is_in_boundary(position):
    x, y = position
    return -5 <= x <= 5 and -5 <= y <= 5


def solution(dirs):
    visited = set()
    position = (0, 0)

    delta_position = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    counter = 0
    for direction in dirs:
        x, y = position
        dx, dy = delta_position[direction]
        nx, ny = x + dx, y + dy

        if not is_in_boundary((nx, ny)):
            continue

        direction_from_to = min((x, y), (nx, ny)) + max((x, y), (nx, ny))
        if direction_from_to not in visited:
            counter += 1
            visited.add(direction_from_to)

        position = (nx, ny)

    return counter


if __name__ == "__main__":
    dirs = "ULURRDLLU"
    assert solution(dirs) == 7

    dirs = "LULLLLLLU"
    assert solution(dirs) == 7

    dirs = "RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU"
    assert solution(dirs) == 11
