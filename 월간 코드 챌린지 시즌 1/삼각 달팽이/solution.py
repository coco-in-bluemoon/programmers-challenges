from collections import deque


def be_in_boundary(position, board):
    r, c = position
    R = len(board)
    C = len(board[r]) if r < R else 0

    return 0 <= r < R and 0 <= c < C


def solution(n):
    board = [[0] * size for size in range(1, n+1)]
    counter = 1
    target = (n * (n+1)) // 2
    r, c = 0, 0
    direction = 0
    deltas = [(1, 0), (0, 1), (-1, -1)]

    while counter <= target:
        board[r][c] = counter
        counter += 1

        dr, dc = deltas[direction]
        if not be_in_boundary((r+dr, c+dc), board) or board[r+dr][c+dc]:
            direction = (direction + 1) % len(deltas)
            dr, dc = deltas[direction]
        r, c = r+dr, c+dc

    return sum(board, [])


if __name__ == "__main__":
    answer = [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
    assert solution(4) == answer

    answer = [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
    assert solution(5) == answer
