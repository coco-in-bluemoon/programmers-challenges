from collections import deque


def be_in_boundary(position, board):
    r, c = position
    R = len(board)
    C = len(board[0])

    return 0 <= r < R and 0 <= c < C


def be_blocked(position, board):
    r, c = position
    return not board[r][c]


def solution(maps):
    R = len(maps)
    C = len(maps[0])

    visited = [[False] * C for _ in range(R)]
    queue = deque([(0, 0, 1)])

    while queue:
        r, c, counter = queue.popleft()
        if visited[r][c]:
            continue

        if r == R-1 and c == C-1:
            return counter

        visited[r][c] = True

        for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nr, nc = r+dr, c+dc

            if not be_in_boundary((nr, nc), maps):
                continue
            if be_blocked((nr, nc), maps):
                continue
            if visited[nr][nc]:
                continue

            queue.append((nr, nc, counter+1))

    return -1


if __name__ == "__main__":
    maps = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]
    assert solution(maps) == 11

    maps = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    assert solution(maps) == -1
