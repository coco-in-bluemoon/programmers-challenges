from collections import deque


def in_boundary(r, c, N):
    return 0 <= r < N and 0 <= c < N


def blocked(r, c, board):
    return board[r][c]


def calculate_cost(cost, r, c, nr, nc, dir):
    if dir == 'R' or dir == 'L':
        if r == nr:
            return (cost + 100, 'R') if c < nc else (cost + 100, 'L')
        else:
            return (cost + 600, 'D') if r < nr else (cost + 600, 'U')
    elif dir == 'U' or dir == 'D':
        if r == nr:
            return (cost + 600, 'R') if c < nc else (cost + 600, 'L')
        else:
            return (cost + 100, 'D') if r < nr else (cost + 100, 'U')


def bfs_cost(board, initial_dir):
    N = len(board)
    queue = deque([(0, 0, initial_dir, 0)])
    cost_mat = [[0] * N for _ in range(N)]

    while queue:
        r, c, dir, cost = queue.popleft()

        for dr, dc in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nr, nc = r + dr, c + dc

            if not in_boundary(nr, nc, N):
                continue

            if blocked(nr, nc, board):
                continue

            next_cost, next_dir = calculate_cost(cost, r, c, nr, nc, dir)

            if not cost_mat[nr][nc] or cost_mat[nr][nc] > next_cost:
                cost_mat[nr][nc] = next_cost
                queue.append((nr, nc, next_dir, next_cost))

    return cost_mat[N-1][N-1]


def solution(board):
    cost_right = bfs_cost(board, 'R')
    cost_down = bfs_cost(board, 'D')

    return min(cost_right, cost_down)


if __name__ == "__main__":
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert solution(board) == 900

    board = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 3800

    board = [
        [0, 0, 1, 0], [0, 0, 0, 0],
        [0, 1, 0, 1], [1, 0, 0, 0]
    ]
    assert solution(board) == 2100

    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    assert solution(board) == 3200
