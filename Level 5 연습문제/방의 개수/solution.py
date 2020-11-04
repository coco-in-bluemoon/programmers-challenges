def solution(arrows):
    delta_r = [-1, -1, 0, 1, 1, 1, 0, -1]
    delta_c = [0, 1, 1, 1, 0, -1, -1, -1]

    r, c = 0, 0
    visited_position = set([(r, c)])
    visited_direction = set()

    counter = 0

    for arrow in arrows:
        dr = delta_r[arrow]
        dc = delta_c[arrow]

        for _ in range(2):
            nr, nc = r+dr, c+dc
            direction = (min((r, c), (nr, nc)), max((r, c), (nr, nc)))

            if (nr, nc) in visited_position:
                if direction not in visited_direction:
                    counter += 1
            visited_position.add((nr, nc))
            visited_direction.add(direction)
            r, c = nr, nc

    return counter


if __name__ == "__main__":
    arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    assert solution(arrows) == 3

    arrows = [1, 5, 2, 0, 5, 0, 4, 2, 1]
    assert solution(arrows) == 1
